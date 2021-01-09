import sys
import math

EPS = 10 ** (-50)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        x_ret = self.x + other.x
        y_ret = self.y + other.y
        return Point(x_ret, y_ret)

    def sub(self, other):
        x_ret = self.x - other.x
        y_ret = self.y - other.y
        return Point(x_ret, y_ret)


class Vector:
    def __init__(self, point):
        self.x = point.x
        self.y = point.y

    def add(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y

    def sub(self, other):
        self.x = self.x - other.x
        self.y = self.y - other.y

    def dot_prod(self, other):
        return self.x * other.x + self.y * other.y

    def cross_prod(self, other):
        return self.x * other.y - self.y * other.x


def angle_with_vector(v1, v2):
    return math.atan2(v1.cross_prod(v2), v1.dot_prod(v2))


def points_on_line(p0, p1, p2, eps=EPS):
    v1 = Vector(point=p1.sub(p0))
    v2 = Vector(point=p2.sub(p0))
    if abs(v1.cross_prod(v2)) < eps:
        return True
    return False


def triangle_area(p0, p1, p2):
    v1 = Vector(point=p1.sub(p0))
    v2 = Vector(point=p2.sub(p0))
    return v1.cross_prod(v2) / 2


def figure_area(p_list):
    area = 0
    for i in range(1, len(p_list) - 1):
        area += triangle_area(p_list[0], p_list[i], p_list[i + 1])
    return abs(area)


def main():
    n = int(sys.stdin.readline())
    point_list = []
    for _ in range(n):
        p_x, p_y = list(map(int, sys.stdin.readline().split(' ')))
        point_list.append(Point(p_x, p_y))
    answer = figure_area(point_list)
    sys.stdout.write(str(answer))


if __name__ == '__main__':
    main()
