
def main(a, n):
    sl1 = 0
    for j in range(1, n+1):
        for c in range(1, a+1):
            sl1 += 90 * j ** 3 + 47 * c ** 5 + 77 * c ** 3
    sl2 = 1
    for c in range(1, n+1):
        x = 0
        for k in range(1, a+1):
            x += 1 - 96 * c ** 7 - k ** 3
        sl2 *= x
    return sl1 + sl2
