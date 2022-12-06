from readBinaryFromFile import binaries

counts = [0] * len(binaries[0])

mostBinary = binaries.copy()
gamma = ''
for ind in range(len(binaries[0])):
    bits = [entry[ind] for entry in mostBinary]
    gamma += '1' if bits.count('1') >= len(binaries)/2 else '0'

epsilon = ''
for ind in range(len(gamma)):
    match gamma[ind]:
        case '1':
            epsilon+='0'
        case _:
            epsilon+='1'

print(int(gamma, 2)*int(epsilon, 2))