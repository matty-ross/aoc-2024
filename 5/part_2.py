import functools


rules = []
page_numbers = []


def check_order(nums: list[int]) -> bool:
    for rule in rules:
        try:
            a_index = nums.index(rule[0])
            b_index = nums.index(rule[1])
            if a_index >= b_index:
                return False
        except ValueError:
            continue
    return True


def order(nums: list[int]) -> None:
    def x(a: int, b: int) -> int:
        for rule in rules:
            if rule[0] == a and rule[1] == b:
                return -1
            if rule[1] == a and rule[0] == b:
                return 1
        return 0
    
    nums.sort(key=functools.cmp_to_key(x))


reading_rules = True
with open('5/input.txt') as fp:
    for line in fp:
        if len(line.strip()) == 0:
            reading_rules = False
        else:
            if reading_rules:
                a, b = line.strip().split('|')
                rules.append((int(a), int(b)))
            else:
                nums = []
                for n in line.strip().split(','):
                    nums.append(int(n))
                page_numbers.append(nums)

s = 0

for nums in page_numbers:
    if not check_order(nums):
        order(nums)
        s += nums[len(nums) // 2]

print(s)
