// Problem: Find a string
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
// Solved on: 2026-10-28T15:22:46.945Z


def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count += 1
    return count
