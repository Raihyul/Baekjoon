import math
import sys
L, A, B, C, D = map(int, sys.stdin.read().strip().split())
print(L-math.ceil(max(A/C, B/D)))