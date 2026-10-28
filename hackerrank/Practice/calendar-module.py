// Problem: Calendar Module
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
// Solved on: 2026-10-28T15:31:56.653Z


import calendar

month, day, year = map(int, input().split())

print(calendar.day_name[calendar.weekday(year, month, day)].upper())
