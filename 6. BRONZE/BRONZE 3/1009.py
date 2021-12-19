for i in range(int(input())):
    a, b = map(int, input().split())
    if a % 10 == 0:
        print(10)
    else:
        print((a%10) ** ((b+3)%4+1) % 10)