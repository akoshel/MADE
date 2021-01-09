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


def cross_lines(p_a, p_b, p_c, p_d):
    v_ab = Vector(point=p_b.sub(p_a))
    v_ac = Vector(point=p_c.sub(p_a))
    v_ad = Vector(point=p_d.sub(p_a))
    v_cd = Vector(point=p_d.sub(p_c))
    v_ca = Vector(point=p_a.sub(p_c))
    v_cb = Vector(point=p_b.sub(p_c))
    if (v_ab.cross_prod(v_ac)) * (v_ab.cross_prod(v_ad)) <= 0 and (v_cd.cross_prod(v_ca)) * (v_cd.cross_prod(v_cb)) <= 0:
        if points_on_line(p_a, p_b, p_c) and points_on_line(p_a, p_b, p_d):
            return point_in_bounds(p_a, p_c, p_d) or point_in_bounds(p_b, p_c, p_d) or \
                    point_in_bounds(p_c, p_a, p_b) or point_in_bounds(p_d, p_a, p_b)
        return True
    return False


def main():
    v1_coords = list(map(int, sys.stdin.readline().split(' ')))
    v2_coords = list(map(int, sys.stdin.readline().split(' ')))
    p_a = Point(v1_coords[0], v1_coords[1])
    p_b = Point(v1_coords[2], v1_coords[3])
    p_c = Point(v2_coords[0], v2_coords[1])
    p_d = Point(v2_coords[2], v2_coords[3])
    if cross_lines(p_a, p_b, p_c, p_d):
        sys.stdout.write("YES")
    else:
        sys.stdout.write("NO")


if __name__ == '__main__':
    main()
