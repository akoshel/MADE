import sys

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


def points_on_line(p0, p1, p2, eps=EPS):
    v1 = Vector(point=p1.sub(p0))
    v2 = Vector(point=p2.sub(p0))
    if abs(v1.cross_prod(v2)) < eps:
        return True
    return False


def coord_in_bounds(x, x_min, x_max):
    if x_min > x_max:
        x_min, x_max = x_max, x_min
    if x_min <= x <= x_max:
        return True
    else:
        return False


def point_in_bounds(p, pb1, pb2):
    if coord_in_bounds(p.x, pb1.x, pb2.x) and coord_in_bounds(p.y, pb1.y, pb2.y):
        return True
    return False


def main():
    coords = list(map(int, sys.stdin.readline().split(' ')))
    points_list = []
    for i in range(len(coords) // 2):
        points_list.append(Point(coords[i * 2], coords[i * 2 + 1]))

    if points_on_line(points_list[0], points_list[1], points_list[2]) and \
            point_in_bounds(points_list[0], points_list[1], points_list[2]):
        sys.stdout.write("YES")
    else:
        sys.stdout.write("NO")


if __name__ == '__main__':
    main()
