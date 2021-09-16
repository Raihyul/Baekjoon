# 14681. 사분면 고르기
X = int(input())
Y = int(input())

if X*Y > 0:
    if X > 0:
        print(1)
    else:
        print(3)
else:
    if X < 0:
        print(2)
    else:
        print(4)