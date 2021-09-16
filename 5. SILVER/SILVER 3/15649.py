# 15649 N과 M (1)

from sys import stdin
from itertools import permutations

N, M = map(int, stdin.readline().split())

#print(*list(map(' '.join, permutations(list(map(str, range(1, N+1))), M))), sep='\n')
print(*list(map(' '.join, permutations(map(str, range(1, N+1)),M))), sep='\n')
'''
from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

def func(data):
    if len(data) == M:
        stdout.write(' '.join(map(str, data)) + '\n')
        return
    for i in range(1, N+1):
        if i not in data:
            data.append(i)
            func(data)
            data.pop()

func([])
'''