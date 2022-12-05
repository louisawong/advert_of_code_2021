from readInstructionsFromFile import instructions

x = y = aim = 0

for instruction in instructions:
    direction = instruction[0]
    move = int(instruction[1])
    match direction:
        case 'forward':
            x+=move
            y+=(aim*move)
        case 'down':
            aim+=move
        case 'up':
            aim-=move

print(x*y)