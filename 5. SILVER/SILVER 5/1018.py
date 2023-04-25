'''
# 1018. 체스판 다시 칠하기
import sys

m, n = map(int, sys.stdin.readline().split()) # 세로, 가로 체스판 사이즈

chess = [[0] for i in range(m)]

for i in range(m):
    chess[i] = list(map(str, sys.stdin.readline().rstrip()))

res = []

for i in range(m-7): # 세로
    for j in range(n-7): # 가로
        chosen = []
        for l in range(8):
            if l % 2 == 0:
                chosen = chosen + chess[i+l][j:j+8]
            else:
                chosen = chosen + chess[i+l][j:j+8][::-1]
        colored = 0
        for k in range(64):
            if k % 2 == 0:
                if chosen[k] != 'B':
                    colored += 1
            else:
                if chosen[k] != 'W':
                    colored += 1
        res.append(colored)
    
print(min(min(res), 64-max(res)))
'''

'''
import sys

ans1 = ["W", "B"]*4
ans2 = ["B", "W"]*4
ANS = []
for _ in range(4):
    ANS.append(ans1)
    ANS.append(ans2)

M, N = map(int, sys.stdin.readline().split()) # 세로, 가로 체스판 사이즈

chess = []

for i in range(M):
    chess.append(list(map(str, sys.stdin.readline().rstrip())))

res = 64

for i in range(M-7): # 세로
    for j in range(N-7): # 가로
        tmp = 0
        for x in range(8):
            for y in range(8):
                if chess[i+x][j+y] != ANS[x][y]:
                    tmp += 1
        res = min(res, tmp, (64-tmp))

print(res)
'''

import sys
from numpy import array

# 정답 체스판 만들기
ans1 = ["W", "B"]*4
ans2 = ["B", "W"]*4
ANS = []
for _ in range(4):
    ANS.append(ans1)
    ANS.append(ans2)

M, N = map(int, sys.stdin.readline().split()) # 세로, 가로 체스판 사이즈

chess = []

# 체스판 현황 입력받기
for i in range(M):
    chess.append(list(map(str, sys.stdin.readline().rstrip())))

gap = [[64 for i in range(10)] for j in range(3)]
# 차이가 가장 적은 5개를 갯수 차이, row, col 순으로 저장한 것

# B, W가 고루 있는 곳을 추출
for i in range(M-7):
    for j in range(N-7):
        tmp = array(chess)[i:i+8,j:j+8]
        gap_tmp = abs((tmp=='B').sum() - (tmp=='W').sum())
        if max(gap[0]) > gap_tmp:
            gap[0][gap[0].index(max(gap[0]))] = gap_tmp
            gap[1][gap[0].index(max(gap[0]))] = i
            gap[2][gap[0].index(max(gap[0]))] = j

res = 64

for row in gap[1]:
    for col in gap[2]:
        tmp = 0
        for x in range(8):
            for y in range(8):
                if chess[row+x][col+y] != ANS[x][y]:
                    tmp += 1
        res = min(res, tmp, (64-tmp))

print(res)