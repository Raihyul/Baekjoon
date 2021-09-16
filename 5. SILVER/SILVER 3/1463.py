# 1463. 1로 만들기

num = input()
cnt = 0

while int(num) > 1:
    if int(num) % 3 == 1:
        num = str(int(num) - 1)
        cnt += 1
    elif sum(map(int, num)) % 3 == 0:
        num = str(int(num) // 3)
        cnt += 1
    elif int(num[-1]) % 2 == 0:
        num = str(int(num) // 2)
        cnt += 1
    else:
        num = str(int(num) - 1)
        cnt += 1

print(cnt)