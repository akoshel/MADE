def get_v(v_prev: int, n: int, r: int, i:int) -> int:
    """Returns v"""
    K1 = 13
    K2 = 593
    K3 = 5
    return ((K1 * v_prev + K2 + r + K3 * i) % n) + 1

print(get_v(9, 10, 570265, 1))
#1 3 9 570265