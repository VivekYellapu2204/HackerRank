// Problem: Designer Door Mat
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
// Solved on: 2026-10-27T14:55:42.152Z


n, m = map(int, input().split())

for i in range(n // 2):
    pattern = '.|.' * (2 * i + 1)
    print(pattern.center(m, '-'))

print('WELCOME'.center(m, '-'))

for i in range(n // 2 - 1, -1, -1):
    pattern = '.|.' * (2 * i + 1)
    print(pattern.center(m, '-'))
