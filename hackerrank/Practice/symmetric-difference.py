// Problem: Symmetric Difference
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true
// Solved on: 2026-10-28T15:36:50.478Z


M = int(input())
set_M = set(map(int, input().split()))

N = int(input())
set_N = set(map(int, input().split()))

for num in sorted(set_M.symmetric_difference(set_N)):
    print(num)
