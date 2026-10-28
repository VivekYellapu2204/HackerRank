// Problem: Lists
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true
// Solved on: 2026-10-28T15:15:58.136Z


if __name__ == '__main__':
    N = int(input())
    arr = []

    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            arr.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(arr)
        elif command[0] == "remove":
            arr.remove(int(command[1]))
        elif command[0] == "append":
            arr.append(int(command[1]))
        elif command[0] == "sort":
            arr.sort()
        elif command[0] == "pop":
            arr.pop()
        elif command[0] == "reverse":
            arr.reverse()
