'''
chess = list(map(int, input().split()))
chess_ans = [1, 1, 2, 2, 2, 8]
chess_less = []

for i in range(len(chess)):
    chess_less.append(chess_ans[i] - chess[i])

print(*chess_less)
'''

chess = list(map(int, input().split()))
chess_ans = [1, 1, 2, 2, 2, 8]

for i in range(len(chess)):
    print(chess_ans[i] - chess[i], end=' ')