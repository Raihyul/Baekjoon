import sys
num_list = list(map(int, sys.stdin.read().strip().split()))
for i in range(len(num_list))[::2]:
    print(num_list[i]+num_list[i+1])