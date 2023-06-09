def main(y, z):
    n = len(y)
    f = 0
    for i in range(n):
        i += 1
        f += (54 * y[n - i] - z[n - i]
              ** 3 - 16 * z[n - i] ** 2) ** 3
    return 81 * f

