// Problem: Collections.OrderedDict()
// Platform: hackerrank
// Language: pypy3
// Verdict: Accepted
// URL: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
// Solved on: 2026-10-28T15:35:38.508Z


from collections import OrderedDict

items = OrderedDict()

for _ in range(int(input())):
    *name, price = input().split()
    item = " ".join(name)
    items[item] = items.get(item, 0) + int(price)

for item, price in items.items():
    print(item, price)
