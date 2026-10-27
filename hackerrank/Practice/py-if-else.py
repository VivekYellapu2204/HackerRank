// Problem: Python If-Else
// Platform: hackerrank
// Language: python3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
// Solved on: 2026-10-27T14:37:48.219Z

n = int(input().strip())

if n % 2 != 0:
    # If n is odd, print Weird[cite: 1]
    print("Weird")
elif 2 <= n <= 5:
    # If n is even and in the inclusive range of 2 to 5, print Not Weird[cite: 1]
    print("Not Weird")
elif 6 <= n <= 20:
    # If n is even and in the inclusive range of 6 to 20, print Weird[cite: 1]
    print("Weird")
else:
    # If n is even and greater than 20, print Not Weird[cite: 1]
    print("Not Weird")
