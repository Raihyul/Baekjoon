# 15650 N과 M (2)

from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

def func(data, last):
    if len(data) == M:
        stdout.write(' '.join(map(str, data)) + '\n')
        return
    for i in range(last+1, N+1):
        # last+1을 한 것은 자기 자신이 겹치지 않도록 하기 위함
        if i not in data:
            data.append(i)
            func(data, i)
            data.pop()

func([], 0)

'''
from sys import stdin
from itertools import combinations
N,M = map(int, stdin.readline().split())
print(*list(map(' '.join, combinations(map(str, range(1, N+1)),M))), sep='\n')
'''