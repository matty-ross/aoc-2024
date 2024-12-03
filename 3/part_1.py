import re


with open('3/input.txt') as fp:
    string = fp.read()

s = 0

matches = re.findall(r'mul\((\d+),(\d+)\)', string)
for a, b in matches:
    s += int(a) * int(b)

print(s)
