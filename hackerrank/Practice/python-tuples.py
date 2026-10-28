// Problem: Tuples
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true
// Solved on: 2026-10-28T15:18:02.163Z


if __name__ == '__main__':
    n = int(input())
    values = tuple(map(int, input().split()))

    mask = (1 << 64) - 1
    x = 0x345678
    mult = 1000003

    for i, value in enumerate(values):
        if value == -1:
            value = -2
        x = ((x ^ value) * mult) & mask
        mult = (mult + 82520 + 2 * (n - i - 1)) & mask

    x = (x + 97531) & mask

    if x >= (1 << 63):
        x -= (1 << 64)
    if x == -1:
        x = -2

    print(x)
