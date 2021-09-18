import sys
time = sum(map(int, sys.stdin.read().strip().split()))
print(time//60, time%60, sep='\n')