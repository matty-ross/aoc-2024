left = []
right = []

with open('1/input.txt', 'r') as fp:
    for line in fp:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))

s = 0
for l in left:
    s += l * right.count(l)

print(s)
