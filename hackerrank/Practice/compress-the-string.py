// Problem: Compress the String!
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
// Solved on: 2026-10-27T15:33:07.875Z


from itertools import groupby

s = input().strip()

result = []
for key, group in groupby(s):
    count = len(list(group))
    result.append((count, int(key)))

print(*result)
