# 1330. 두 수 비교하기

import sys

A, B = map(int, sys.stdin.readline().split())

print('>' if A>B else '<' if A<B else '==')