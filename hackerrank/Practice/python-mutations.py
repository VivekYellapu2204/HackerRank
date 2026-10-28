// Problem: Mutations
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
// Solved on: 2026-10-28T15:22:08.514Z

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]

