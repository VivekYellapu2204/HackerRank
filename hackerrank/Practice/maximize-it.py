// Problem: Maximize It!
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true
// Solved on: 2026-10-27T15:17:38.046Z


from itertools import product

K, M = map(int, input().split())

lists = []
for _ in range(K):
    values = list(map(int, input().split()))
    lists.append([x * x for x in values[1:]])

print(max(sum(combination) % M for combination in product(*lists)))
