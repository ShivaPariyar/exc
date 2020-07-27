import re

file = open("D:actual.txt")
for line in file:
    line = line.rstrip()
    if re.search("From:",line):
        print(line)

hand = open("D:actual.txt")
for line in hand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)

if re.findall("From: ([^ ]+:)", line):