a = int(input())
b = int(input())
c = int(input())

mul = str(a*b*c)
cnt = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}

for n in mul:
    cnt[n] += 1

print(*list(cnt.values()), sep='\n')

'''
# list의 count 함수를 사용하는 방법
d = list(map(int, (str(a * b * c))))

for i in range(10):
    print(d.count(i))

# 10으로 나눈 나머지를 카운팅하는 방법도 있음
'''