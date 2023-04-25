import sys
import time

N = int(sys.stdin.readline())

info = []

for i in range(N):
    info.append(list(map(int, sys.stdin.readline().split())))

res = []

for x in info:
    rank = 1
    for y in info:
        if x[0] < y[0] and x[1] < y[1]:
            rank += 1
    res.append(str(rank))

start1 = time.time()

result = " ".join(res)
print(result)

print("time1 :", time.time() - start1)

start2 = time.time()

print(*res, sep = ' ')

print("time2 :", time.time() - start2)