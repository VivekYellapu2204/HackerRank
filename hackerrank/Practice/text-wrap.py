// Problem: Text Wrap
// Platform: hackerrank
// Language: python3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
// Solved on: 2026-10-27T14:54:42.145Z



def wrap(string, max_width):
    # Wrap the string into a paragraph of the given width using textwrap.fill[cite: 16]
    return textwrap.fill(string, max_width)

