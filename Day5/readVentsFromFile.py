with open('input.txt', 'r') as file:
    lines = file.read().splitlines()
    ventLines = [line.strip().split('->') for line in lines]