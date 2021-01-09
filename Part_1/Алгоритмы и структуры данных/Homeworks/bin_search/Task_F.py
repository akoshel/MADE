import sys

def get_distance(a, b):
    return((a**2 + b**2)**0.5)

def ternary_search(v_field, v_forest, a):
    field_high = 1 - a
    forest_high = a
    l = 0
    r = 1
    fi = (1 + 5**0.5) / 2
    m1 = l + (r - l) / (fi + 1)
    m2 = r - (r - l) / (fi + 1)
    field_distance1 = get_distance(m1, field_high)
    forest_distance1 = get_distance(1 - m1, forest_high)
    field_distance2 = get_distance(m2, field_high)
    forest_distance2 = get_distance(1 - m2, forest_high)
    t1 = (field_distance1 / v_field) + (forest_distance1 / v_forest)
    t2 = (field_distance2 / v_field) + (forest_distance2 / v_forest)
    for i in range(100):
        if t1 < t2:
            r = m2
            m2 = m1
            t2 = t1
            m1 = l + ((r - l) / (fi + 1))
            field_distance1 = get_distance(m1, field_high)
            forest_distance1 = get_distance(1 - m1, forest_high)
            t1 = (field_distance1 / v_field) + (forest_distance1 / v_forest)
        else:
            l = m1
            m1 = m2
            t1 = t2
            m2 = r - ((r - l) / (fi + 1))
            field_distance2 = get_distance(m2, field_high)
            forest_distance2 = get_distance(1 - m2, forest_high)
            t2 = (field_distance2 / v_field) + (forest_distance2 / v_forest)
    return r

v_field, v_forest = list(map(int, sys.stdin.readline().split(' ')))
a = float(sys.stdin.readline())
sys.stdout.write(str(ternary_search(v_field, v_forest, a)))

