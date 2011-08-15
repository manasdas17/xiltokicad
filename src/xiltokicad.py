#!/usr/bin/env python

path = "../data/xiltest.txt"

f = open(path, "r")
data = f.readlines()
f.close()

print data

y = 4

"""
strings zerlegen und in einzelne listen schreiben, und zwar als dictionary
like: 144 -> ['0', 'TL', 'IO_L1P_HSWAPEN_0']
"""

pins = {}

while data[y] != '\n':
    print data[y]
    partedline = data[y].split('\t')
    data[y] = [partedline[1], partedline[2], partedline[3].strip()]
    partedline[0] = partedline[0].strip('P')
    pins[partedline[0]] = data[y]
    #print pins
    y = y + 1

for key in pins:
    print key, pins[key]

"""
funktion um aus einem dictionary einzelne schaltplanfiguren zu bauen, aufgeteilt nach 
"""
