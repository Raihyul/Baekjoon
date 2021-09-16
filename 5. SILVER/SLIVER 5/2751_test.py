from sys import stdin, stdout

N = stdin.readline()
arr = map(int, stdin.read().split())
print(arr)
stdout.write('\n'.join(map(str,arr)))

# N = int(stdin.readline())
# _list = []
# for i in range(N):
#     _list.append(int(stdin.readline()))
# stdout.write('\n'.join(map(str,sorted(_list))))