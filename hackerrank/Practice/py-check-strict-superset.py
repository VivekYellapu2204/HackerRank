// Problem: Check Strict Superset
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true
// Solved on: 2026-10-27T15:12:52.930Z


A = set(map(int, input().split()))
n = int(input())

result = True

for _ in range(n):
    other = set(map(int, input().split()))
    if not A > other:
        result = False
        break

print(result)
