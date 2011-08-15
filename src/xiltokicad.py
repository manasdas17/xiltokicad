#!/usr/bin/env python

"""
function to get pins from extracted lines
returns a dictionary like: {<pinnumber>:[<BANK>, <BUFIO2 Clocking Region>, <Pinname>]}
"""
def getPinsFromLines(data):
    y = 4
    pins = {}
    while data[y] != '\n':
        print data[y]
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
            banks[value[0]] = 0
    return banks

"""
funktion um aus einem dictionary einzelne schaltplanfiguren zu bauen, aufgeteilt nach 
"""
def drawPins():
    return False


"""
funktion um den header der lib zu schreiben, z.B.:
EESchema-LIBRARY Version 2.3  Date: Mon 15 Aug 2011 11:35:57 PM CEST
"""
def writeLibHeader():
    return "EESchema-Library 2.3"

"""
function to read the whole file and stor its conten in a list (line by line)
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
    


main()