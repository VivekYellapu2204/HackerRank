// Problem: String Formatting
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
// Solved on: 2026-10-27T14:57:02.415Z

def print_formatted(number):
    width = len(bin(number)[2:])

    for i in range(1, number + 1):
        print(
            str(i).rjust(width),
            oct(i)[2:].rjust(width),
            hex(i)[2:].upper().rjust(width),
            bin(i)[2:].rjust(width)
        )



