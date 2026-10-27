// Problem: ginortS
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true
// Solved on: 2026-10-27T15:10:46.689Z


s = input()

lowercase = sorted(c for c in s if c.islower())
uppercase = sorted(c for c in s if c.isupper())
odd_digits = sorted(c for c in s if c.isdigit() and int(c) % 2 == 1)
even_digits = sorted(c for c in s if c.isdigit() and int(c) % 2 == 0)

print(''.join(lowercase + uppercase + odd_digits + even_digits))
