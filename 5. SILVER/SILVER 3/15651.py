# 15651. N과 M (3)
'''
from sys import stdin, stdout

N, M = map(int, stdin.readline().split())

arr = [1 for i in range(M-1)]
arr.append(0)

while sum(arr) < N*M:
    arr[-1] += 1
    for i in range(M-1,0,-1):
        if arr[i] > N:
            arr[i-1] += 1
            arr[i] -= N
    stdout.write(' '.join(map(str, arr)) + '\n')
'''


def DFS(x, res, check):
    if x == m: # 왜 global 선언을 안했는데 사용이 될까????
        print(res)
        return
    for i in range(1, n+1):
        check[i] = True
        DFS(x+1, res + str(i) + ' ', check)
        check[i] = False

if __name__ == "__main__":
    n, m = map(int, input().split())
    check = [False for _ in range(n+1)]
    res = ''
    DFS(0, res, check)





import itertools
N,M = map(int,input().split())
list1 = list(map(str,range(1,N+1)))

print("\n".join(list(map(" ".join,itertools.product(list1,repeat=M)))))