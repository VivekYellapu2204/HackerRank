// Problem: Introduction to Sets
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true
// Solved on: 2026-10-28T15:29:07.052Z

def average(array):
    distinct_heights = set(array)
    return round(sum(distinct_heights) / len(distinct_heights), 3)
