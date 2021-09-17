import sys

sys.stdin.readline()
_list = set(sys.stdin.readline().split())

sys.stdin.readline()
for num in list(sys.stdin.readline().split()):
    if num in _list:
        print(1)
    else:
        print(0)