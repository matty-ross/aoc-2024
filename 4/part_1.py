def search_left_right(lines: list[str]) -> int:
    count = 0
    for r in range(len(lines)):
        for c in range(len(lines[0]) - 3):
            if lines[r][c + 0] == 'X' and lines[r][c + 1] == 'M' and lines[r][c + 2] == 'A' and lines[r][c + 3] == 'S':
                count += 1
    return count

def search_right_left(lines: list[str]) -> int:
    count = 0
    for r in range(len(lines)):
        for c in reversed(range(3, len(lines[0]))):
            if lines[r][c - 0] == 'X' and lines[r][c - 1] == 'M' and lines[r][c - 2] == 'A' and lines[r][c - 3] == 'S':
                count += 1
    return count

def search_up_down(lines: list[str]) -> int:
    count = 0
    for c in range(len(lines[0])):
        for r in range(len(lines) - 3):
            if lines[r + 0][c] == 'X' and lines[r + 1][c] == 'M' and lines[r + 2][c] == 'A' and lines[r + 3][c] == 'S':
                count += 1
    return count

def search_down_up(lines: list[str]) -> int:
    count = 0
    for c in range(len(lines[0])):
        for r in reversed(range(3, len(lines))):
            if lines[r - 0][c] == 'X' and lines[r - 1][c] == 'M' and lines[r - 2][c] == 'A' and lines[r - 3][c] == 'S':
                count += 1
    return count

def search_left_right_up_down(lines: list[str]) -> int:
    count = 0
    for r in range(len(lines) - 3):
        for c in range(len(lines[0]) - 3):
            if lines[r + 0][c + 0] == 'X' and lines[r + 1][c + 1] == 'M' and lines[r + 2][c + 2] == 'A' and lines[r + 3][c + 3] == 'S':
                count += 1
    return count

def search_right_left_up_down(lines: list[str]) -> int:
    count = 0
    for r in range(len(lines) - 3):
        for c in reversed(range(3, len(lines[0]))):
            if lines[r + 0][c - 0] == 'X' and lines[r + 1][c - 1] == 'M' and lines[r + 2][c - 2] == 'A' and lines[r + 3][c - 3] == 'S':
                count += 1
    return count

def search_left_right_down_up(lines: list[str]) -> int:
    count = 0
    for r in reversed(range(3, len(lines))):
        for c in range(len(lines[0]) - 3):
            if lines[r - 0][c + 0] == 'X' and lines[r - 1][c + 1] == 'M' and lines[r - 2][c + 2] == 'A' and lines[r - 3][c + 3] == 'S':
                count += 1
    return count

def search_right_left_down_up(lines: list[str]) -> int:
    count = 0
    for r in reversed(range(3, len(lines))):
        for c in reversed(range(3, len(lines[0]))):
            if lines[r - 0][c - 0] == 'X' and lines[r - 1][c - 1] == 'M' and lines[r - 2][c - 2] == 'A' and lines[r - 3][c - 3] == 'S':
                count += 1
    return count


lines = []
with open('4/input.txt') as fp:
    for line in fp:
        lines.append(line.strip())

count = 0
count += search_left_right(lines)
count += search_right_left(lines)
count += search_up_down(lines)
count += search_down_up(lines)
count += search_left_right_up_down(lines)
count += search_right_left_up_down(lines)
count += search_left_right_down_up(lines)
count += search_right_left_down_up(lines)

print(count)
