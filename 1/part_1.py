left = []
right = []

with open('1/input.txt', 'r') as fp:
    for line in fp:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()

s = 0
for l, r in zip(left, right):
    s += abs(l - r)

print(s)
