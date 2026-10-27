// Problem: Reduce Function
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true
// Solved on: 2026-10-27T15:46:56.117Z



def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

