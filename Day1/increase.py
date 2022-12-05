from readSonarMeasurementsFromFile import sonarMeasurements

previousSonarMeasurements = sonarMeasurements[0]
counter = 0
for measurement in sonarMeasurements:
    if measurement > previousSonarMeasurements:
        counter+=1
    previousSonarMeasurements = measurement

print(counter)