// Problem: Find Angle MBC
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
// Solved on: 2026-10-27T15:30:26.416Z


import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan(AB / BC))
print(str(round(angle)) + chr(176))
