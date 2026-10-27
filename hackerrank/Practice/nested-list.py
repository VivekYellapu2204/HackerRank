// Problem: Nested Lists
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
// Solved on: 2026-10-27T15:02:37.888Z

if __name__ == '__main__':
    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    second_lowest = sorted(set(score for name, score in records))[1]

    names = sorted(name for name, score in records if score == second_lowest)

    for name in names:
        print(name)
