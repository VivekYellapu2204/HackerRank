// Problem: String Formatting
// Platform: hackerrank
// Language: python3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
// Solved on: 2026-10-27T14:56:55.158Z

def print_formatted(number):
    # Determine the padding width based on the binary representation of number[cite: 19]
    width = len(bin(number)[2:])
    
    # Print Decimal, Octal, Hexadecimal (capitalized), and Binary for each i from 1 to number[cite: 19]
    for i in range(1, number + 1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")
