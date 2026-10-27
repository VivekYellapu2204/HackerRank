// Problem: Alphabet Rangoli
// Platform: hackerrank
// Language: python3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
// Solved on: 2026-10-27T14:58:07.334Z

import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    lines = []
    width = 4 * size - 3
    
    for i in range(size):
        # Generate the characters from the outer letter down to the current inner letter and back
        s = '-'.join(alphabet[size - 1 : i : -1] + alphabet[i : size])
        lines.append(s.center(width, '-'))
        
    # Combine the top half, center, and bottom half
    print('\n'.join(lines[::-1] + lines[1:]))
