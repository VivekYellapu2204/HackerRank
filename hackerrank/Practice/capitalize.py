// Problem: Capitalize!
// Platform: hackerrank
// Language: python3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
// Solved on: 2026-10-27T14:59:04.333Z



def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

