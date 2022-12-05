from readInstructionsFromFile import instructions

x = y = 0

for instruction in instructions:
    direction = instruction[0]
    move = int(instruction[1])
    match direction:
        case 'forward':
            x+=move
        case 'down':
            y+=move
        case 'up':
            y-=move

print(x*y)