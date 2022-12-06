from readBinaryFromFile import binaries

oxygenBinaries = binaries.copy()
for ind in range(len(oxygenBinaries[0])):
    if len(oxygenBinaries) == 1:
        break
    oxygenBits = [binary[ind] for binary in oxygenBinaries]
    commonOxygenBit = '1' if oxygenBits.count('1') >= len(oxygenBinaries)/2 else '0'
    oxygenBinaries = [binary for binary in oxygenBinaries
        if binary[ind]==commonOxygenBit]
    oxygen= int(oxygenBinaries[0], 2)

co2Binaries = binaries.copy()
for ind in range(len(co2Binaries[0])):
    if len(co2Binaries) == 1:
        break
    co2Bits = [binary[ind] for binary in co2Binaries]
    commonCo2Bit = '0' if co2Bits.count('1') >= len(co2Binaries)/2 else '1'
    co2Binaries = [ binary for binary in co2Binaries
        if binary[ind]==commonCo2Bit]
    co2 = int(co2Binaries[0], 2)

print(co2*oxygen)
