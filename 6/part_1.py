from enum import Enum
from dataclasses import dataclass


@dataclass
class GuardPosition:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))


class GuardDirection(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Map:
    
    def __init__(self, area):
        self.area = area
        self.guard_position = None
        self.guard_positions = set()
        self.guard_direction = GuardDirection.NORTH
        
        for r in range(len(area)):
            for c in range(len(area[r])):
                if self.area[r][c] == '^':
                    self.guard_position = GuardPosition(c, r)
                    self.guard_positions.add(self.guard_position)
        assert self.guard_position is not None
    

    def do_guard_step(self) -> bool:
        self._check_bostacle()
        match self.guard_direction:
            case GuardDirection.NORTH:
                self.guard_position.y -= 1
            case GuardDirection.EAST:
                self.guard_position.x += 1
            case GuardDirection.SOUTH:
                self.guard_position.y += 1
            case GuardDirection.WEST:
                self.guard_position.x -= 1
        if self._is_guard_in_area():
            self.guard_positions.add(self.guard_position)
            return True
        return False

    
    def _check_bostacle(self) -> None:
        x, y = (self.guard_position.x, self.guard_position.y)
        match self.guard_direction:
            case GuardDirection.NORTH:
                if y > 0 and self.area[y - 1][x] == '#':
                    self.guard_direction = GuardDirection.EAST
            case GuardDirection.EAST:
                if x < (len(self.area[0]) - 1) and self.area[y][x + 1] == '#':
                    self.guard_direction = GuardDirection.SOUTH
            case GuardDirection.SOUTH:
                if y < (len(self.area) - 1) and self.area[y + 1][x] == '#':
                    self.guard_direction = GuardDirection.WEST
            case GuardDirection.WEST:
                if x > 0 and self.area[y][x - 1] == '#':
                    self.guard_direction = GuardDirection.NORTH

    
    def _is_guard_in_area(self) -> bool:
        x, y = (self.guard_position.x, self.guard_position.y)
        if x < 0 or x >= len(area[0]):
            return False
        if y < 0 or y >= len(area):
            return False
        return True


area = []
with open('6/input.txt') as fp:
    for line in fp:
        area.append(line.strip())

m = Map(area)
while m.do_guard_step():
    pass

print(len(m.guard_positions))
