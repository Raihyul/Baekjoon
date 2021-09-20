num1, num2 = map(int, input().split())
num1, num2 = str(num1)[::-1] + '0'*len(str(num2)), str(num2)[::-1] + '0'*len(str(num1))
tmp = 0
ans = ''

for i in range(len(num1)):
    if tmp + int(num1[i]) + int(num2[i]) > 1:
        ans += str(tmp + int(num1[i]) + int(num2[i]) - 2)
        tmp = 1
    else:
        ans += str(tmp + int(num1[i]) + int(num2[i]))
        tmp = 0

print(int(ans[::-1]))

'''
a, b = map(str, input().split())
ans = int(a, 2) + int(b, 2)

print(format(ans, 'b'))
'''