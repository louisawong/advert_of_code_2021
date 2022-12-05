from readSonarMeasurementsFromFile import sonarMeasurements

counter = sum(
    sonarMeasurements[i] > sonarMeasurements[i-3]
    for i in range(3, len(sonarMeasurements))
)

print(counter)