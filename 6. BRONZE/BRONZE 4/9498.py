# 9498. 시험 성적

import sys

score = int(sys.stdin.readline())

print("A" if score>=90 else "B" if score>=80 else "C" if score>=70 else "D" if score>=60 else "F")

# print('FFFFFFDCBAA'[int(input())//10])