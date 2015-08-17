#! /usr/bin/env python3

import sys
import array

width = 2080

SYNC = [
    -14, -14, -14,
    18, 18, -14, -14, 18, 18, -14, -14, 18, 18, -14, -14,
    18, 18, -14, -14, 18, 18, -14, -14, 18, 18, -14, -14,
    18, 18, -14, -14, -14
]

def corr(i):
    r = 0.0
    for j in range(len(SYNC)):
        r += buf[i + j] * SYNC[int(j)]
    return r

with open(sys.argv[1], 'rb') as file:
    buf = array.array('f', file.read())
out = array.array('B')

#equalize
max = 0;
for i in range(len(buf)):
    if buf[i] > max:
        max = buf[i]
for i in range(len(buf)):
    buf[i] = buf[i] / max

max = 0
for i in range(len(buf) - len(SYNC)-9):
    r = corr(i+4)
    if r > max:
        max = r
    if r > 45 and corr(i) < r and corr(i+1) < r and corr(i+2) < r and corr(i+3) < r and corr(i+5) < r and corr(i+6) < r and corr(i+7) < r and corr(i+8) < r:
        out += array.array('B', [abs(int(x * 255)) for x in buf[i:i + width]])
        i += width - 10

len = int(len(out) / width)
with open(sys.argv[2], 'wb') as file:
    file.write((
"""P5
%d %d
255
""" % (width, len)
    ).encode('utf-8')) #PGM
    out[:width * len].tofile(file)
