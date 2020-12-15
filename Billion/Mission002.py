#!/usr/bin/env python3

import json

# https://tracking-game.reaktor.com/parts/per/billion
# Used rapidtables.com to convert binary to ASCII/UTF-8
# and saved it as Mission002.json

rawJsonHandle = open("Mission002.json")
rawJsonData = rawJsonHandle.read()
rawData = json.loads(rawJsonData)
rawJsonHandle.close()

# Structure:
# rawData[0]
#  'date' : '1-Dec-2018'
#  'readings': [
#    'time': 0
#    'id': '7D643075F3DD43'
#    'contaminants': [
#      '#B48': 359011
#      '#16F': 40255
#      and so on

totals = []

for dayData in rawData:
    for reading in dayData['readings']:
        total = 0
        for substance in reading['contaminants']:
            total += reading['contaminants'][substance]
        totals.append([total, reading['id']])

# We end up with a list of lists:
# [1007342, 'D87E5645F3C192']
# [1007706, 'C522188B90B15B']
# [1007424, 'B38587A8372B63']
# [1003367, '42A318979448E5']

# Just by eyeballing it I assumed that the standard
# range is around 1,000,000 - 1,010,000

for reading in totals:
    if reading[0] > 1010000:
        print(reading[1])

# python3 Mission002.py | xxd -r -p
