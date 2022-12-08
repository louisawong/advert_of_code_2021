with open('input.txt', 'r') as file:
    lines = file.read()
    caller, *board = lines.split('\n\n')
    calls = [int(call) for call in caller.split(',')]