import re


enabled_spans = []


def in_enabled_spans(span: tuple[int, int]) -> bool:
    for enabled_span in enabled_spans:
        if span[0] >= enabled_span[0] and span[1] <= enabled_span[1]:
            return True
    return False


with open('3/input.txt') as fp:
    string = fp.read()

enabled = True
index = 0
while index < len(string):
    if enabled:
        start = index
        end = string.find("don't()", index)
        if end == -1:
            end = len(string)
        index = end
        enabled_spans.append((start, end))
        enabled = False
    else:
        index = string.find('do()', index)
        if index == -1:
            index = len(string)
        enabled = True

s = 0

matches = re.finditer(r'mul\((\d+),(\d+)\)', string)
for match in matches:
    if in_enabled_spans(match.span()):
        a, b = match.groups()
        s += int(a) * int(b)

print(s)
