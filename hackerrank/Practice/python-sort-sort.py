// Problem: Athlete Sort
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true
// Solved on: 2026-10-27T15:08:18.669Z

#!/bin/python3

import math
import os
import random
import re
import sys




if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    k = int(input())

    arr.sort(key=lambda row: row[k])

    for row in arr:
        print(*row)

