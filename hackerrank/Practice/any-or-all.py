// Problem: Any or All
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true
// Solved on: 2026-10-27T15:09:25.629Z


n = int(input())
numbers = list(map(int, input().split()))

print(all(x > 0 for x in numbers) and any(str(x) == str(x)[::-1] for x in numbers))
