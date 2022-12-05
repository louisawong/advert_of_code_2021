with open('input.txt', 'r') as file:
    lines = file.readlines()
    instructions = [line.split() for line in lines]