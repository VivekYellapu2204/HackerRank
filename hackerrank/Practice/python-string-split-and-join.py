// Problem: String Split and Join
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
// Solved on: 2026-10-28T15:19:40.947Z



def split_and_join(line):
    # write your code here
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
