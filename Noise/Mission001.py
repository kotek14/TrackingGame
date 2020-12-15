#!/usr/bin/env python3

# https://tracking-game.reaktor.com/signal/vs/noise

scrambledHandle = open("Mission001.input")
scrambledSignal = scrambledHandle.read()
scrambledHandle.close()

index = 0

# Using slices to get chunks of 16 characters
# Using set() to remove duplicates from every chunk
# If the length of that set is still 16, there were no diplicates.

while index < len(scrambledSignal) - 16:
    chunk = scrambledSignal[index:index + 16]
    if len(set(chunk)) == 16:
        print(chunk)
        exit(0)
    index += 1

# python3 Mission001.py | base64 -d
