import sys

_list = list(map(int, sys.stdin.read().split()))
sys.stdout.write(str(max(_list)) + '\n' + str(_list.index(max(_list))+1))