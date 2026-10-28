// Problem: Polar Coordinates
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
// Solved on: 2026-10-28T15:27:52.733Z


import cmath

z = complex(input())

print(abs(z))
print(cmath.phase(z))
