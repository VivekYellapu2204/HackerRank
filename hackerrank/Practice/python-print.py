// Problem: Print Function
// Platform: hackerrank
// Language: python3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
// Solved on: 2026-10-27T14:49:46.594Z

if __name__ == '__main__':
    n = int(input())
    
    # Print integers from 1 through n without spaces or string methods[cite: 10]
    for i in range(1, n + 1):
        print(i, end="")
