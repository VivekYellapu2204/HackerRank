// Problem: Default Arguments
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/default-arguments/problem?isFullScreen=true
// Solved on: 2026-10-27T15:16:24.081Z


class EvenStream:
    def __init__(self):
        self.current = 0

    def get_next(self):
        self.current += 2
        return self.current - 2


class OddStream:
    def __init__(self):
        self.current = -1

    def get_next(self):
        self.current += 2
        return self.current


def print_from_stream(n, stream=EvenStream()):
    for _ in range(n):
        print(stream.get_next())


if __name__ == '__main__':
    queries = int(input())

    for _ in range(queries):
        stream_name, n = input().split()
        n = int(n)

        if stream_name == "even":
            print_from_stream(n)
        else:
            print_from_stream(n, OddStream())
