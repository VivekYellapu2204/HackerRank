// Problem: Find the Runner-Up Score!
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
// Solved on: 2026-10-27T15:00:58.094Z

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    scores = sorted(set(arr))
    print(scores[-2])
