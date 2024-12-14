from dataclasses import dataclass


@dataclass
class Vec2:
    x: int
    y: int


@dataclass
class Robot:
    position: Vec2
    velocity: Vec2


class Space:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.robots: list[Robot] = []


    def debug_print(self) -> None:
        for y in range(self.height):
            for x in range(self.width):
                count = 0
                for robot in self.robots:
                    if robot.position.x == x and robot.position.y == y:
                        count += 1
                print(count if count > 0 else '.', end='')
            print()


    def tick(self) -> None:
        for robot in self.robots:
            self._move_robot(robot)


    def get_robots_in_quadrant(self, quadrant: int) -> list[Robot]:
        if quadrant == 1:
            top = Vec2(0, 0)
            bottom = Vec2(self.width // 2 - 1, self.height // 2 - 1)
            return self._get_robots_in_area(top, bottom)
        if quadrant == 2:
            top = Vec2(self.width // 2 + 1, 0)
            bottom = Vec2(self.width - 1, self.height // 2 - 1)
            return self._get_robots_in_area(top, bottom)
        if quadrant == 3:
            top = Vec2(0, self.height // 2 + 1)
            bottom = Vec2(self.width // 2 - 1, self.height - 1)
            return self._get_robots_in_area(top, bottom)
        if quadrant == 4:
            top = Vec2(self.width // 2 + 1, self.height // 2 + 1)
            bottom = Vec2(self.width - 1, self.height - 1)
            return self._get_robots_in_area(top, bottom)
        assert False, "What ya doin?"


    def _move_robot(self, robot: Robot) -> None:
        robot.position.x += robot.velocity.x
        robot.position.y += robot.velocity.y

        x, y = robot.position.x, robot.position.y
        if x < 0:
            x += self.width
        elif x >= self.width:
            x -= self.width
        if y < 0:
            y += self.height
        elif y >= self.height:
            y -= self.height
        robot.position.x, robot.position.y = x, y


    def _get_robots_in_area(self, top: Vec2, bottom: Vec2) -> list[Robot]:
        robots = []
        for robot in self.robots:
            position = robot.position
            if position.x >= top.x and position.x <= bottom.x and position.y >= top.y and position.y <= bottom.y:
                robots.append(robot)
        return robots


space = Space(101, 103)

with open('14/input.txt') as fp:
    for line in fp:
        p, v = line.strip().split()
        px, py = p.replace('p=', '').split(',')
        vx, vy = v.replace('v=', '').split(',')
        robot = Robot(
            position=Vec2(int(px), int(py)),
            velocity=Vec2(int(vx), int(vy)),
        )
        space.robots.append(robot)

for _ in range(100):
    space.tick()
# space.debug_print()

safety_factor = 1
safety_factor *= len(space.get_robots_in_quadrant(1))
safety_factor *= len(space.get_robots_in_quadrant(2))
safety_factor *= len(space.get_robots_in_quadrant(3))
safety_factor *= len(space.get_robots_in_quadrant(4))

print(safety_factor)
