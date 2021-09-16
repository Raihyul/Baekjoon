# 1003. 피보나치 함수

def fibonacci(n):
    ans = ''
    if n == 0 or n == 1:
        return ans + str(n)
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for _ in range(int(input())):
    num = int(input())
    print(fibonacci(num))



'''
from sys import stdin

N = int(stdin.readline())

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibo = [[0, 1],
        [1, 1],
        [1, 2],
        [1, 3],
        [2, 3]]

for _ in range(N):
    num = int(stdin.readline())
    
    if num == 0:
        print("1 0")
    else:
        num = fibonacci(num)

        ans0 = (num//5) * 2 + fibo[num%5 - 1][0]
        ans1 = (num//5) * 3 + fibo[num%5 - 1][1]

        print(ans0, ans1)
'''
'''
for _ in range(int(input())):
    ans = [1, 0]
    num = int(input())
    if num == 0:
        print(*ans, sep=' ')
    else:
        for i in range(num):
            ans = [ans[1], sum(ans)]
        print(*ans, sep=' ')
'''

'''
# 은수님 코드
import sys

n = int(sys.stdin.readline())

def fibonacci(n):
    #[0 호출 수, 1 호출 수]  
        
    fibo = [[0,0] for _ in range(n+1)]
    fibo[0][0] = 1
    
    if n > 0:
        fibo[1][1] = 1
        for i in range(2, n+1):
            fibo[i][0] = fibo[i-1][0] + fibo[i-2][0]
            fibo[i][1] = fibo[i-1][1] + fibo[i-2][1]
        
    print(fibo[n][0], fibo[n][1])

for _ in range(n):
    t = int(sys.stdin.readline())
    fibonacci(t)
'''

'''
# 준호님 참고 중인 코드
zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[num], one[num]))

T = int(input())

for _ in range(T):
    fibonacci(int(input()))
'''