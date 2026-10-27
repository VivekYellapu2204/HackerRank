// Problem: Merge the Tools!
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
// Solved on: 2026-10-27T15:27:01.769Z

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        result = ""
        
        for char in substring:
            if char not in result:
                result += char
        
        print(result)


