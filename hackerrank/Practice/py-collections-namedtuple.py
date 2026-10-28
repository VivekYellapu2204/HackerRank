// Problem: Collections.namedtuple()
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
// Solved on: 2026-10-28T15:33:28.580Z


from collections import namedtuple

N = int(input())
Student = namedtuple('Student', input().split())

students = [Student(*input().split()) for _ in range(N)]
print(f"{sum(int(s.MARKS) for s in students) / N:.2f}")
