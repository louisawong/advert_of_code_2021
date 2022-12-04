with open('input.txt', 'r') as file:
    lines = file.readlines()
    sonarMeasurements = [int(measurement) for measurement in lines]

previousSonarMeasurements = sonarMeasurements[0]
counter = 0
for measurement in sonarMeasurements:
    if measurement > previousSonarMeasurements:
        counter+=1
    previousSonarMeasurements = measurement

print(counter)