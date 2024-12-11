with open('11/input.txt') as fp:
    stones = [int(stone) for stone in fp.readline().strip().split()]

for _ in range(25):
    new_stones = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            l = len(s) // 2
            new_stones.append(int(s[:l]))
            new_stones.append(int(s[l:]))
        else:
            new_stones.append(stone * 2024)

    stones = new_stones

print(len(stones))
