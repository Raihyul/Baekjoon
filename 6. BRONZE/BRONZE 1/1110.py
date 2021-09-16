'''
num_origin = input()
num = num_origin if len(num_origin) == 2 else '0' + num_origin

cnt = 0

while True:
    num = (num[-1]) + str(int(num[0]) + int(num[1]))[-1]
    cnt += 1
    if int(num) == int(num_origin):
        print(cnt)
        break
'''

num_origin = int(input())
num = -1
cnt = 0

while num_origin != num:
    if num == -1:
        num = num_origin
    num = {(num//10 + num%10)%10 + (num%10)*10}
    cnt += 1

print(cnt)