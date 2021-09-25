h, m, s = map(int, input().split())
t = int(input()) + h * 3600 + m * 60 + s
print((t//3600)%24, (t%3600)//60, t%60)