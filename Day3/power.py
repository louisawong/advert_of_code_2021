from readBinaryFromFile import binaries

counts = [0] * len(binaries[0])

halfLength = len(binaries)/2

for binary in binaries:
    for index, position in enumerate(binary):
        if position == '1':
            counts[index]+=1

gamma = epsilon = ''

for count in counts:
    if (count>halfLength):
        gamma += '1'
        epsilon += '0'
    else:
       gamma += '0'
       epsilon += '1' 

print(int(gamma, 2)*int(epsilon, 2))