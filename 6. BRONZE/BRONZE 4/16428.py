import sys
A, B = map(int, sys.stdin.readline().split())
if B < 0:
    print(A//B+1, A%B-B, sep='\n')
else:
    print(A//B, A%B, sep='\n')