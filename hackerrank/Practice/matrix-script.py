// Problem: Matrix Script
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/matrix-script/problem?isFullScreen=true
// Solved on: 2026-10-27T15:23:34.045Z


import re

n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

decoded = ''.join(matrix[i][j] for j in range(m) for i in range(n))
print(re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded))
