// Problem: Company Logo
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
// Solved on: 2026-10-27T15:36:16.283Z

#!/bin/python3

import math
import os
import random
import re
import sys


from collections import Counter

if __name__ == '__main__':
    s = input().strip()

    counts = Counter(s)

    for char, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:3]:
        print(char, count)
