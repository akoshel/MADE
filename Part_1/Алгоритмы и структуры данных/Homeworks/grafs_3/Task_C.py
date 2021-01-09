import sys


def prime(points, n):
    used = {i: False for i in range(n)}
    dist = {i: float('Inf') for i in range(n)}
    dist[0] = 0
    next_v = -1
    ost_length = 0
    for _ in range(n):
        min_weight = float('Inf')
        for ind in range(n):
            if next_v == -1 or ((not used[ind]) and (dist[ind] < min_weight)):
                min_weight = dist[ind]
                next_v = ind
        for i in range(n):
            new_root = ((points[i][0] - points[next_v][0]) ** 2 +
                        (points[i][1] - points[next_v][1]) ** 2)
            dist[i] = min(dist[i], new_root)
        ost_length += min_weight ** 0.5
        used[next_v] = True
    return ost_length


def main() -> None:
    n = int(sys.stdin.readline())
    points = []
    for _ in range(n):
        points.append(list(map(int, sys.stdin.readline().split(' '))))
    sys.stdout.write(str(prime(points, n)))


if __name__ == '__main__':
    main()
