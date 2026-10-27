// Problem: XML 1 - Find the Score
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/xml-1-find-the-score/problem?isFullScreen=true
// Solved on: 2026-10-27T15:13:52.877Z



def get_attr_number(node):
    score = len(node.attrib)
    for child in node:
        score += get_attr_number(child)
    return score

