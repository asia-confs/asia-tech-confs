#!/usr/bin/env python3

import sys

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()


translations = [
    ("台灣", "Taiwan"),
    ("台北", "Taipei"),
    ("北京", "Beijing"),
    ("中國", "China"),
    ("日本", "Japan"),
    ("南京", "Nanjing"),
    ("北海道", "Hokkaido"),
    ("名古屋", "Nagoya"),
    ("大阪", "Osaka"),
    ("新加坡", "Singapore"),
    ("東京", "Tokyo"),
    ("沖繩", "Okinawa"),
    ("香港", "Hong Kong"),
    ("浜名湖,", "Lake Hamana"),
]

tmp = lines
for trans in translations:
    tmp = list(map(lambda l: l.replace(trans[0], trans[1]), tmp))
    tmp = tmp


print("".join(tmp))
