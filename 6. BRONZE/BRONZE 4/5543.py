import sys

price = list(map(int, sys.stdin.read().rstrip().split()))
print(min(price[0:3])+min(price[3:5])-50)