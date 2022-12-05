with open('input.txt', 'r') as file:
    lines = file.readlines()
    sonarMeasurements = [int(measurement) for measurement in lines]