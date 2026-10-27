// Problem: Validating Credit Card Numbers
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/validating-credit-card-number/problem?isFullScreen=true
// Solved on: 2026-10-27T15:49:22.366Z


import re

n = int(input())

for _ in range(n):
    card = input().strip()

    if re.fullmatch(r'[456]\d{15}|[456]\d{3}(-\d{4}){3}', card):
        digits = card.replace('-', '')
        if not re.search(r'(\d)\1{3,}', digits):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
