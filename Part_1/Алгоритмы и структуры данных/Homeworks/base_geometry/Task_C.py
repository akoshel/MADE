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


def vector_angle(v1, v2):
    return math.atan2(v1.cross_prod(v2), v1.dot_prod(v2))


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


def point_in_segment(p, p1_segment, p2_segment):
    return points_on_line(p, p1_segment, p2_segment) and point_in_bounds(p, p1_segment, p2_segment)


def point_in_fig(p, points, eps=EPS):
    item = points[-1]
    for item_next in points:
        if (p.x == item_next.x and p.y == item_next.y) or point_in_segment(p, item, item_next):
            return True
        item = item_next

    v0 = Vector(point=points[-1].sub(p))
    v_next = Vector(point=points[0].sub(p))
    angle_sum = vector_angle(v0, v_next)
    for i in range(1, len(points)):
        v0 = v_next
        v_next = Vector(point=points[i].sub(p))
        angle_sum += vector_angle(v0, v_next)
    if abs(abs(angle_sum) / math.pi - 2.0) < eps:
        return True
    else:
        return False


def main():
    n, p_x, p_y = list(map(int, sys.stdin.readline().split(' ')))
    p = Point(p_x, p_y)
    point_list = []
    for _ in range(n):
        p_x, p_y = list(map(int, sys.stdin.readline().split(' ')))
        point_list.append(Point(p_x, p_y))

    if point_in_fig(p, point_list, eps=0.0001):
        sys.stdout.write("YES")
    else:
        sys.stdout.write("NO")


if __name__ == '__main__':
    main()
