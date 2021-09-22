a, b = map(int, input().split())
c = int(input())
print((a+((b+c)//60))%24, (b+c)%60)

'''
h,m=map(int,input().split())
t=h*60+m+int(input())
print(t//60%24,t%60)
'''