# For my love kimsa

heart_pattern = [
    "  ***   ***  ",
    " ***** ***** ",
    "*************",
    " *********** ",
    "  *********  ",
    "   *******   ",
    "    *****    ",
    "     ***     ",
    "      *      ",
]

# Repeat "I love you " enough times to cover the heart shape
phrase = "I love you " * 100
char_index = 0

heart_text = []
for line in heart_pattern:
    current_line = ""
    for char in line:
        if char == "*":
            current_line += phrase[char_index % len(phrase)]
            char_index += 1
        else:
            current_line += " "
    heart_text.append(current_line)

print("\n".join(heart_text))
