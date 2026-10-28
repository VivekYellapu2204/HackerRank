// Problem: Exceptions
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true
// Solved on: 2026-10-28T15:33:15.875Z


for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error Code: {e}")
