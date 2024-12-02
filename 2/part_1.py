def is_sorted(levels: list[int]) -> bool:
    if all(levels[i] < levels[i + 1] for i in range(len(levels) - 1)):
        return True
    if all(levels[i] > levels[i + 1] for i in range(len(levels) - 1)):
        return True
    return False


def is_safe(levels: list[int]) -> bool:
    if not is_sorted(levels):
        return False

    if levels[0] < levels[1]:
        for i in range(len(levels) - 1):
            if (levels[i + 1] - levels[i]) > 3:
                return False
            
    if levels[0] > levels[1]:
        for i in range(len(levels) - 1):
            if (levels[i] - levels[i + 1]) > 3:
                return False
            
    return True


s = 0
with open('2/input.txt') as fp:
    for line in fp:
        levels = [int(level) for level in line.split()]
        if is_safe(levels):
            s += 1

print(s)
