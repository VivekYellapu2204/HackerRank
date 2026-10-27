// Problem: Write a function
// Platform: hackerrank
// Language: python3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
// Solved on: 2026-10-27T14:48:13.444Z

def is_leap(year):
    leap = False
    
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
        
    return leap
