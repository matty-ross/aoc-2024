with open('9/input.txt') as fp:
    disk_map = fp.readline().strip()

blocks = []
id = 0
for i, size in enumerate(disk_map):
    if i % 2 == 0:
        for _ in range(int(size)):
            blocks.append(id)
        id += 1
    else:
        for _ in range(int(size)):
            blocks.append('.')

l = 0
r = len(blocks) - 1

while l < r:
    if blocks[l] != '.':
        l += 1
        continue
    if blocks[r] == '.':
        r -= 1
        continue
    blocks[l] = blocks[r]
    blocks[r] = '.'

checksum = 0
for i, c in enumerate(blocks):
    if c == '.':
        break
    checksum += i * int(c)

print(checksum)
