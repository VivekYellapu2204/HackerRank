// Problem: Text Alignment
// Platform: hackerrank
// Language: python3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true
// Solved on: 2026-10-27T14:53:29.555Z

thickness = int(input())  # Must be an odd number[cite: 14]
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))
