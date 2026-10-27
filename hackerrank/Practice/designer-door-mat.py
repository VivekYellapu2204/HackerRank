// Problem: Designer Door Mat
// Platform: hackerrank
// Language: python3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true
// Solved on: 2026-10-27T14:55:35.788Z

n, m = map(int, input().split())

# Top half
for i in range(1, n, 2):
    print(('.|.' * i).center(m, '-'))

# Middle line
print('WELCOME'.center(m, '-'))

# Bottom half
for i in range(n - 2, 0, -2):
    print(('.|.' * i).center(m, '-'))
