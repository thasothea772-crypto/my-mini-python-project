import pygame
import math
import random

pygame.init()

W, H = 800, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("PYTHON PROGRAMMING COURSE")

CX, CY = W // 2, H // 2

rocks = []
for i in range(700):
    angle = random.uniform(0, math.pi * 2)
    radius = random.uniform(150, 310)
    
    rocks.append({
        "angle": angle,
        "radius": radius,
        "target": radius,
        "speed": random.uniform(0.0005, 0.002),
        "size": random.choice([1, 1, 1, 2, 2, 3])
    })

clock = pygame.time.Clock()
time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time += 0.025
    
    screen.fill((2, 4, 10))
    
    planet_progress = min(time / 4.5, 1)
    planet_radius = 15 + 105 * planet_progress
    planet_radius += math.sin(time * 2) * 1.5
    
    glow = pygame.Surface((W, H), pygame.SRCALPHA)
    
    for r in range(int(planet_radius + 40), int(planet_radius), -5):
        alpha = int((1 - (r - planet_radius) / 40) * 15)
        pygame.draw.circle(
            glow,
            (80, 130, 180, alpha),
            (CX, CY),
            r
        )
    screen.blit(glow, (0, 0))
    
    for i in range(25):
        ring_r = 150 + i * 6
        
        pygame.draw.circle(
            screen,
            (30, 45, 70),
            (CX, CY),
            int(ring_r),
            1
        )

    for p in rocks:
        p["target"] = random.uniform(150, 310)
        p["radius"] += (p["target"] - p["radius"]) * 0.02
        p["angle"] += p["speed"]
        
        x = CX + math.cos(p["angle"]) * p["radius"]
        y = CY + math.sin(p["angle"]) * p["radius"] * 0.35
        
        if y > CY:
            brightness = int(100 + math.sin(p["angle"]) * 50)
            pygame.draw.circle(
                screen,
                (55, 75, 100),
                (int(x), int(y)),
                p["size"]
            )

    pygame.draw.circle(
        screen,
        (120, 160, 190),
        (CX, CY),
        int(planet_radius),
        2
    )
    
    light_angle = time * 0.7
    lx = CX + math.cos(light_angle) * planet_radius * 0.55
    ly = CY + math.sin(light_angle) * planet_radius * 0.45

    for i in range(25):
        a = time * 0.7 + i * 0.25
        shine = math.sin(time * 2) + 1 / 2
        
        pygame.draw.circle(
            screen,
            (
                min(255, int(100 + shine * 100)),
                min(255, int(120 + shine * 120)),
                255
            ),
            (int(lx), int(ly)),
            2
        )

    for p in rocks:
        x = CX + math.cos(p["angle"]) * p["radius"]
        y = CY + math.sin(p["angle"]) * p["radius"] * 0.35
        abs_ck = abs(int(CX) - x) > 350
        if abs_ck or abs(y - CY) > 150:
            pass

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

import pygame
import math
import random

pygame.init()

W, H = 800, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Planet Simulation")

CX, CY = W // 2, H // 2

rocks = []
for i in range(700):
    angle = random.uniform(0, math.pi * 2)
    radius = random.uniform(150, 310)
    
    rocks.append({
        "angle": angle,
        "radius": radius,
        "target": radius,
        "speed": random.uniform(0.0005, 0.002),
        "size": random.choice([1, 1, 1, 2, 2, 3])
    })

clock = pygame.time.Clock()
time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time += 0.025
    
    screen.fill((2, 4, 10))
    
    planet_progress = min(time / 4.5, 1)
    planet_radius = 15 + 105 * planet_progress
    planet_radius += math.sin(time * 2) * 1.5
    
    glow = pygame.Surface((W, H), pygame.SRCALPHA)
    
    # Glow effect circles
    for r in range(int(planet_radius + 40), int(planet_radius), -5):
        alpha = int((1 - (r - planet_radius) / 40) * 15)
        pygame.draw.circle(
            glow,
            (80, 130, 180, alpha),
            (CX, CY),
            r
        )
    screen.blit(glow, (0, 0))
    
    # Draw background rings and orbit lines
    for i in range(25):
        ring_r = 150 + i * 6
        ring_progress = min(time / 3, 1)
        
        pygame.draw.circle(
            screen,
            (30, 45, 70),
            (CX, CY),
            int(ring_r),
            1
        )

    # Update and draw background rocks/particles
    for p in rocks:
        p["target"] = random.uniform(150, 310)
        p["radius"] += (p["target"] - p["radius"]) * 0.02
        p["angle"] += p["speed"]
        
        x = CX + math.cos(p["angle"]) * p["radius"]
        y = CY + math.sin(p["angle"]) * p["radius"] * 0.35
        
        if y > CY:
            brightness = int(100 + math.sin(p["angle"]) * 50)
            pygame.draw.circle(
                screen,
                (brightness, brightness, min(255, brightness + 15)),
                (int(x), int(y)),
                p["size"]
            )

    # Draw central planet body
    pygame.draw.circle(
        screen,
        (120, 160, 190),
        (CX, CY),
        int(planet_radius),
        2
    )
    
    light_angle = time * 0.7
    lx = CX + math.cos(light_angle) * planet_radius * 0.55
    ly = CY + math.sin(light_angle) * planet_radius * 0.45
    
    pygame.draw.circle(
        screen,
        (200, 220, 240),
        (int(lx), int(ly)),
        int(planet_radius * 0.2)
    )

    # Draw foreground rocks/particles
    for p in rocks:
        x = CX + math.cos(p["angle"]) * p["radius"]
        y = CY + math.sin(p["angle"]) * p["radius"] * 0.35
        
        if y <= CY:
            brightness = int(150 + math.sin(p["angle"]) * 50)
            pygame.draw.circle(
                screen,
                (brightness, brightness, min(255, brightness + 20)),
                (int(x), int(y)),
                p["size"]
            )

    # Additional inner decorative rings loop from video
    for i in range(25):
        a = time * 0.7 + i * 0.25
        shine = math.sin(time * 2 + i) / 2
        # Render extra details matching later lines
        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

import pygame
import math
import random

pygame.init()

W, H = 800, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Planet Simulation")

# Center coordinates
CX, CY = W // 2, H // 2

rocks = []
for i in range(700):
    angle = random.uniform(0, math.pi * 2)
    radius = random.uniform(150, 310)
    
    rocks.append({
        "angle": angle,
        "radius": radius,
        "target": radius,
        "speed": random.uniform(0.0005, 0.002),
        "size": random.choice([1, 1, 1, 2, 2, 3])
    })

clock = pygame.time.Clock()
time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time += 0.025
    
    screen.fill((2, 4, 10))
    
    planet_progress = min(time / 4.5, 1)
    planet_radius = 15 + 105 * planet_progress
    planet_radius = math.sin(time * 2) * 1.5
    
    glow = pygame.Surface((W, H), pygame.SRCALPHA)
    
    # Draw background rings and orbit lines
    for i in range(25):
        ring_r = 150 + i * 6
        ring_progress = min(time / 3, 1)
        
        pygame.draw.circle(
            screen,
            (30, 45, 70),
            (CX, CY),
            int(ring_r),
            1
        )

    # Draw rocks/particles in the rings
    for p in rocks:
        p["angle"] += p["speed"]
        
        x = CX + math.cos(p["angle"]) * p["radius"]
        y = CY + math.sin(p["angle"]) * p["radius"] * 0.35
        
        if y > CY:
            offset = math.sin(time + 0.8) * 1
            # Render background rocks
            pygame.draw.circle(
                screen,
                (55, 75, 100),
                (int(x), int(y)),
                p["size"]
            )

    # Draw central planet body
    pygame.draw.circle(
        screen,
        (120, 160, 190),
        (CX, CY),
        int(planet_radius),
        2
    )
    
    light_angle = time * 0.7
    lx = CX + math.cos(light_angle) * planet_radius * 0.55
    ly = CY + math.sin(light_angle) * planet_radius * 0.45
    
    # Draw foreground rocks
    for p in rocks:
        x = CX + math.cos(p["angle"]) * p["radius"]
        y = CY + math.sin(p["angle"]) * p["radius"] * 0.35
        
        if y <= CY:
            pygame.draw.circle(
                screen,
                (200, 220, 240),
                (int(x), int(y)),
                p["size"]
            )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
