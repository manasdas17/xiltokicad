#!/usr/bin/env python

"""
function to get pins from extracted lines
returns a dictionary like: {<pinnumber>:[<BANK>, <BUFIO2 Clocking Region>, <Pinname>]}
"""
def getPinsFromLines(data):
    y = 4
    pins = {}
    while data[y] != '\n':
        partedline = data[y].split('\t')
        data[y] = [partedline[1], partedline[2], partedline[3].strip()]
        partedline[0] = partedline[0].strip('P')
        pins[partedline[0]] = data[y]
        y = y + 1
    return pins

"""
function to count the different banks in the fpga (NA is a separate bank)
"""
# TODO: sort the damn thing
def countBanks(pins):
    banks = {}
    for value in pins.itervalues():
        if banks.has_key(value[0]):
            banks[value[0]] = banks[value[0]] + 1
        else:
            banks[value[0]] = 1
    return banks

"""
draws all the pins in the symbol
e.g.:
X pin1 0 500 100 150 L 50 50 1 1 I
x <pinname> <pinnumber> <Xpos> <Ypos> <pinlength> <orientation> <Snum> <Sname> <Partnuber> 1 <electrical type>
Snum/Sname: Pinnumber/name textsize (default 50)
"""
def drawPins():
    pinlength = "150"
    pinxpos = "350"
    orientation = "L"
    snum = "50"
    sname = "50"
    eletype = "I"
    return False


"""
funktion um den header der lib zu schreiben, z.B.:
EESchema-LIBRARY Version 2.3  Date: Mon 15 Aug 2011 11:35:57 PM CEST
"""
# TODO: add the date and time of library creation
# TODO: write the full header unti DRAW
def writeLibHeader(name, bankCount):
    header = []
    header.append("EESchema-LIBRARY Version 2.3 \nDEF ")
    # begin DEF row
    header.append(name)
    header.append(" IC 0 40 Y Y ")
    header.append(str(bankCount))
    header.append(" F N\n")
    # end DEF row
    
    # begin field0
    header.append("F0 \"IC\" ")
    # end field0
    
    return ''.join(header)

"""
function to read the whole file and store its content in a list (line by line)
"""
def readData(path):
    f = open(path, "r")
    data = f.readlines()
    f.close()
    return data



def main():
    # data = list of lines in the file
    data = readData("../data/xil_data.txt")
    pins = getPinsFromLines(data)
    bankCount = countBanks(pins)
    
    name = "Spartan6LX9"
    print writeLibHeader(name, len(bankCount))


main()