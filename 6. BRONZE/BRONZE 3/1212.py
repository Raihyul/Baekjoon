'''
# 시간 초과 나는 코드
oNum = input()
bNum = ''

for num in oNum:
    tmp = str(format(int(num), 'b'))
    bNum += '0'*(3-len(tmp)) + tmp

print(int(bNum))
'''

print(format((int(input(), 8)), "b"))