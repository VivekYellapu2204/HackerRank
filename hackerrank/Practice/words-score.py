// Problem: Words Score
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/words-score/problem?isFullScreen=true
// Solved on: 2026-10-27T15:51:31.827Z


def score_words(words):
    vowels = 'aeiouy'
    score = 0

    for word in words:
        count = sum(1 for ch in word if ch in vowels)
        score += 2 if count % 2 == 0 else 1

    return score
