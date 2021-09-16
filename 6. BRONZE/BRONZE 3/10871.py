from sys import stdin, stdout

_, standard = map(int, stdin.readline().split())
_list = list(map(int, stdin.readline().split()))

for num in _list:
    if num < standard:
        stdout.write(f"{num} ")