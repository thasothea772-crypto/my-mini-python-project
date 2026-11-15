import cv2
import mediapipe as mp
import numpy as np
import math
import subprocess
import platform
import sys
import time


OS = platform.system()

def _get_volume_linux() -> int:
    """Return current master volume 0-100 via pactl or amixer."""
    try:
        out = subprocess.check_output(
            ["pactl", "get-sink-volume", "@DEFAULT_SINK@"],
            stderr=subprocess.DEVNULL, text=True
        )
      
        for part in out.split():
            if part.endswith("%"):
                return int(part.rstrip("%"))
    except Exception:
        pass
    try:
        out = subprocess.check_output(
            ["amixer", "sget", "Master"], stderr=subprocess.DEVNULL, text=True
        )
        import re
        m = re.search(r"\[(\d+)%\]", out)
        if m:
            return int(m.group(1))
    except Exception:
        pass
    return 50  

def _set_volume_linux(vol: int):
    vol = max(0, min(100, vol))
    try:
        subprocess.call(
            ["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{vol}%"],
            stderr=subprocess.DEVNULL
        )
        return
    except Exception:
        pass
    try:
        subprocess.call(
            ["amixer", "sset", "Master", f"{vol}%"],
            stderr=subprocess.DEVNULL
        )
    except Exception:
        pass

def _get_volume_mac() -> int:
    try:
        out = subprocess.check_output(
            ["osascript", "-e", "output volume of (get volume settings)"],
            text=True
        )
        return int(out.strip())
    except Exception:
        return 50

def _set_volume_mac(vol: int):
    vol = max(0, min(100, vol))
    subprocess.call(
        ["osascript", "-e", f"set volume output volume {vol}"],
        stderr=subprocess.DEVNULL
    )

def _get_volume_windows() -> int:
    try:
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        return int(volume.GetMasterVolumeLevelScalar() * 100)
    except Exception:
        return 50

def _set_volume_windows(vol: int):
    vol = max(0, min(100, vol))
    try:
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(vol / 100.0, None)
    except Exception:
        pass

if OS == "Darwin":
    get_volume = _get_volume_mac
    set_volume = _set_volume_mac
elif OS == "Windows":
    get_volume = _get_volume_windows
    set_volume = _set_volume_windows
else: 
    get_volume = _get_volume_linux
    set_volume = _set_volume_linux


mp_hands   = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_styles  = mp.solutions.drawing_styles

THUMB_TIP = mp_hands.HandLandmark.THUMB_TIP
INDEX_TIP = mp_hands.HandLandmark.INDEX_FINGER_TIP
WRIST     = mp_hands.HandLandmark.WRIST
MIDDLE_MCP= mp_hands.HandLandmark.MIDDLE_FINGER_MCP


DIST_MIN = 30   
DIST_MAX = 220  


EMA_ALPHA = 0.15  

# Colours  (BGR)
CLR_ACCENT  = (0,  220, 180)  
CLR_LOW     = (60, 100, 255)   
CLR_HIGH    = (0,  200,  60)   
CLR_TEXT    = (240, 240, 240)
CLR_BG_BAR  = (40,  40,  40)
CLR_CIRCLE  = (255, 255, 255)
CLR_LINE    = (180, 180, 255)
CLR_PINCH   = (0,  255, 255)   


def lerp(a, b, t):
    return a + (b - a) * t

def dist2d(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def landmark_px(lm, w, h):
    return int(lm.x * w), int(lm.y * h)

def draw_rounded_rect(img, x1, y1, x2, y2, r, color, thickness=-1):
    cv2.rectangle(img, (x1 + r, y1), (x2 - r, y2), color, thickness)
    cv2.rectangle(img, (x1, y1 + r), (x2, y2 - r), color, thickness)
    for cx, cy in [(x1+r, y1+r), (x2-r, y1+r), (x1+r, y2-r), (x2-r, y2-r)]:
        cv2.circle(img, (cx, cy), r, color, thickness)

def draw_ui(frame, vol_pct: float, raw_dist: float,
            thumb_pt, index_pt, pinching: bool, fps: float):
    h, w = frame.shape[:2]


    overlay = frame.copy()
    panel_x, panel_w, panel_h = w - 200, 180, 200
    draw_rounded_rect(overlay, panel_x, 10, panel_x + panel_w, 10 + panel_h,
                      12, (18, 18, 28), -1)
    cv2.addWeighted(overlay, 0.72, frame, 0.28, 0, frame)

    
    bar_x   = panel_x + 30
    bar_top = 30
    bar_bot = 190
    bar_h   = bar_bot - bar_top
    bar_w   = 22


    draw_rounded_rect(frame, bar_x, bar_top, bar_x + bar_w, bar_bot,
                      6, CLR_BG_BAR, -1)

    # fill
    fill_h  = int(bar_h * vol_pct / 100)
    fill_y  = bar_bot - fill_h
    vol_col = (
        int(lerp(CLR_LOW[0], CLR_HIGH[0], vol_pct / 100)),
        int(lerp(CLR_LOW[1], CLR_HIGH[1], vol_pct / 100)),
        int(lerp(CLR_LOW[2], CLR_HIGH[2], vol_pct / 100)),
    )
    if fill_h > 4:
        draw_rounded_rect(frame, bar_x, fill_y, bar_x + bar_w, bar_bot,
                          6, vol_col, -1)

    # label
    cv2.putText(frame, "VOL", (bar_x - 2, bar_top - 8),
                cv2.FONT_HERSHEY_SIMPLEX, 0.42, CLR_TEXT, 1, cv2.LINE_AA)
    cv2.putText(frame, f"{int(vol_pct)}%", (bar_x - 4, bar_bot + 18),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, vol_col, 2, cv2.LINE_AA)

   
    sp_x, sp_y = panel_x + 100, 80
    
    pts = np.array([[sp_x,sp_y-10],[sp_x+14,sp_y-10],
                    [sp_x+22,sp_y-18],[sp_x+22,sp_y+18],
                    [sp_x+14,sp_y+10],[sp_x,sp_y+10]], np.int32)
    cv2.fillPoly(frame, [pts], CLR_ACCENT)
   
    for r_off, alpha in [(20,255),(32,180),(44,120)]:
        if vol_pct > (r_off - 18) * 2.5:
            col = tuple(int(c * alpha/255) for c in CLR_ACCENT)
            cv2.ellipse(frame, (sp_x+22, sp_y), (r_off, r_off),
                        0, -60, 60, col, 2, cv2.LINE_AA)

    
    db_x1, db_y1 = 20, h - 50
    db_x2, db_y2 = 260, h - 28
    draw_rounded_rect(frame, db_x1, db_y1, db_x2, db_y2, 6, CLR_BG_BAR, -1)
    fill_w = int((db_x2 - db_x1 - 4) * min(raw_dist, DIST_MAX) / DIST_MAX)
    if fill_w > 4:
        draw_rounded_rect(frame, db_x1+2, db_y1+2,
                          db_x1+2+fill_w, db_y2-2, 5, CLR_ACCENT, -1)
    cv2.putText(frame, f"Finger gap: {int(raw_dist)}px",
                (db_x1 + 6, db_y1 - 6),
                cv2.FONT_HERSHEY_SIMPLEX, 0.42, CLR_TEXT, 1, cv2.LINE_AA)

   
    cv2.putText(frame, f"FPS {fps:.0f}", (10, 22),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (100, 200, 100), 1, cv2.LINE_AA)

   
    if thumb_pt and index_pt:
        line_col = CLR_PINCH if pinching else CLR_LINE
        cv2.line(frame, thumb_pt, index_pt, line_col, 2, cv2.LINE_AA)

        mid = ((thumb_pt[0] + index_pt[0]) // 2,
               (thumb_pt[1] + index_pt[1]) // 2)
        # midpoint circle with distance
        cv2.circle(frame, mid, 6, line_col, -1, cv2.LINE_AA)

        # thumb & index dots
        cv2.circle(frame, thumb_pt,  10, CLR_CIRCLE, -1, cv2.LINE_AA)
        cv2.circle(frame, thumb_pt,  10, vol_col,      2, cv2.LINE_AA)
        cv2.circle(frame, index_pt,  10, CLR_CIRCLE, -1, cv2.LINE_AA)
        cv2.circle(frame, index_pt,  10, vol_col,      2, cv2.LINE_AA)

        if pinching:
            cv2.putText(frame, "MUTED / MIN", (mid[0] + 12, mid[1] + 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, CLR_PINCH, 2, cv2.LINE_AA)

    # ── help text ───────────────────────────────────────────────────────────
    cv2.putText(frame, "Pinch = Vol Down   |   Spread = Vol Up   |   Q = Quit",
                (10, h - 8),
                cv2.FONT_HERSHEY_SIMPLEX, 0.38, (130, 130, 130), 1, cv2.LINE_AA)

    return frame


# ─── Main loop ───────────────────────────────────────────────────────────────

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌  Could not open webcam. Check that a camera is connected.")
        sys.exit(1)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)

    current_vol   = float(get_volume())
    smoothed_vol  = current_vol
    last_set_vol  = int(current_vol)
    last_set_time = 0.0
    SET_INTERVAL  = 0.08   # seconds between actual system calls

    prev_time = time.time()

    print("🎚️  Volume Controller running — show your hand to the camera!")
    print("   Pinch thumb & index  →  volume down")
    print("   Spread them apart    →  volume up")
    print("   Press Q or ESC       →  quit\n")

    with mp_hands.Hands(
        model_complexity=0,
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.6,
    ) as hands:

        while True:
            ok, frame = cap.read()
            if not ok:
                break

            frame = cv2.flip(frame, 1)   # mirror
            h, w  = frame.shape[:2]

            rgb    = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)

            thumb_pt  = None
            index_pt  = None
            raw_dist  = 0.0
            pinching  = False

            if result.multi_hand_landmarks:
                lms = result.multi_hand_landmarks[0]

                # Draw skeleton
                mp_drawing.draw_landmarks(
                    frame, lms, mp_hands.HAND_CONNECTIONS,
                    mp_styles.get_default_hand_landmarks_style(),
                    mp_styles.get_default_hand_connections_style(),
                )

                thumb_pt  = landmark_px(lms.landmark[THUMB_TIP],  w, h)
                index_pt  = landmark_px(lms.landmark[INDEX_TIP],  w, h)

                # Normalise distance by hand size (wrist→mid-MCP)
                wrist_pt  = landmark_px(lms.landmark[WRIST],      w, h)
                mmcp_pt   = landmark_px(lms.landmark[MIDDLE_MCP], w, h)
                hand_size = max(dist2d(wrist_pt, mmcp_pt), 1)

                raw_dist  = dist2d(thumb_pt, index_pt)
                pinching  = raw_dist < DIST_MIN + 10

                # Map to volume
                vol_target = np.interp(raw_dist, [DIST_MIN, DIST_MAX], [0, 100])
                vol_target = float(np.clip(vol_target, 0, 100))

                # Smooth
                smoothed_vol += EMA_ALPHA * (vol_target - smoothed_vol)

                # Apply to system (rate-limited)
                now = time.time()
                new_vol_int = int(round(smoothed_vol))
                if abs(new_vol_int - last_set_vol) >= 1 and (now - last_set_time) > SET_INTERVAL:
                    set_volume(new_vol_int)
                    last_set_vol  = new_vol_int
                    last_set_time = now

            # FPS
            now      = time.time()
            fps      = 1.0 / max(now - prev_time, 1e-6)
            prev_time = now

            frame = draw_ui(frame, smoothed_vol, raw_dist,
                            thumb_pt, index_pt, pinching, fps)

            cv2.imshow("🎚️  Volume Controller  (Q to quit)", frame)

            key = cv2.waitKey(1) & 0xFF
            if key in (ord("q"), ord("Q"), 27):  # Q or ESC
                break

    cap.release()
    cv2.destroyAllWindows()
    print("👋  Volume Controller closed.")


if __name__ == "__main__":
    main()