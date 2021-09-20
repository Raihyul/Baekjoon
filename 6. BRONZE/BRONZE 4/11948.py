# science = sorted([int(input()) for _ in range(4)])
# social = sorted([int(input()) for _ in range(2)])
# print(sum(science[-3:]) + social[1])

import sys
score = list(map(int, sys.stdin.read().strip().split()))
print(sum(score) - min(score[:4]) - min(score[4:6]))
