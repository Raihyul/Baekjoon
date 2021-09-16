'''
2231. 분해합

어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다.
물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다.
반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
'''

N = int(input())

num1 = N - (int(str(N)[0]) + (len(str(N))-1)*9)
# num1 = N - (N//(10**math.log10(N)) + math.floor(math.log10(N))*9)

# num2 = N - int(str(N)[0])
# num2 = N - N//(10**math.log10(N))

ANS = False

print(N, num1)

#for num in range(num1, N):
for num in range(N):
    tmp = num
    for i in str(num):
        tmp += int(i)
    #print(tmp)
    if tmp == N:
        ANS = True
        #break
        print(num, tmp)

if ANS:
    print(num)
else:
    print(0)
    
'''
list_tmp = []
for num in range(1, 1001):
    tmp = num
    for i in str(num):
        tmp += int(i)
    list_tmp.append(tmp)

list_tmp.sort()
for i in range(0,1000,10):
    print(list_tmp[i:i+10])
'''