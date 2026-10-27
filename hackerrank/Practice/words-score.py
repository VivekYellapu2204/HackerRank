// Problem: Words Score
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/words-score/problem?isFullScreen=true
// Solved on: 2026-10-27T15:51:51.883Z


def score_words(words):
    vowels = set("aeiouy")
    total = 0

    for word in words:
        count = sum(1 for ch in word if ch in vowels)
        total += 2 if count % 2 == 0 else 1

    return total


if __name__ == '__main__':
    n = int(input().strip())
    words = input().split()
    print(score_words(words))
