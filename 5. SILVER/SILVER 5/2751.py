# 2751. 수 정렬하기 2
'''
import sys

N  = int(sys.stdin.readline())
_list = []

for i in range(N):
    _list.append(int(sys.stdin.readline()))

_list.sort()

#for num in _list:
#    print(num)

print(*_list, sep='\n')
'''

import sys
N = int(sys.stdin.readline())
_list = []
for i in range(N):
    _list.append(int(sys.stdin.readline()))
sys.stdout.write('\n'.join(map(str,sorted(_list))))

'''
from sys import stdin, stdout

stdin.read()
arr = sorted(map(int, stdin.read().split()))
stdout.write('\n'.join(map(str,arr)))
'''