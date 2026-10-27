// Problem: Time Delta
// Platform: hackerrank
// Language: python3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true
// Solved on: 2026-10-27T15:28:18.934Z


import math
import os
import re
import sys
from datetime import datetime


def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"

    time1 = datetime.strptime(t1, fmt)
    time2 = datetime.strptime(t2, fmt)

    return str(int(abs((time1 - time2).total_seconds())))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
