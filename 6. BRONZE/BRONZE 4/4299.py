hap, cha = map(int, input().split())
x, y = hap+cha, hap-cha
if x%2==0 and y%2==0 and y>=0:
    print(x//2, y//2)
else:
    print(-1)