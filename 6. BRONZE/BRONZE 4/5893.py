num = int(input())
num1, num2 = ('0' + str(num) + '0'*4)[::-1], ('0'*5 + str(num))[::-1]
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
a = input()
ans = int(a, 2) * 17

print(format(ans, 'b'))
'''