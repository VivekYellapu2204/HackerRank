// Problem: Input()
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/input/problem?isFullScreen=true
// Solved on: 2026-10-27T15:04:55.400Z


x, k = map(int, input().split())
polynomial = input()

print(eval(polynomial) == k)
