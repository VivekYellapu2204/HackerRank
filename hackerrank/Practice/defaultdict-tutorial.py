// Problem: DefaultDict Tutorial
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
// Solved on: 2026-10-28T15:30:41.572Z


from collections import defaultdict

n, m = map(int, input().split())

group_a = defaultdict(list)

for i in range(1, n + 1):
    word = input().strip()
    group_a[word].append(i)

for _ in range(m):
    word = input().strip()
    if word in group_a:
        print(*group_a[word])
    else:
        print(-1)
