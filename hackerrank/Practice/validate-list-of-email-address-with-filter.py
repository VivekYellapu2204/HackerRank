// Problem: Validating Email Addresses With a Filter
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem?isFullScreen=true
// Solved on: 2026-10-27T15:45:43.623Z

def fun(s):
    import re
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.fullmatch(pattern, s))


