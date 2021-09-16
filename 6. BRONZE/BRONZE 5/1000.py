'''
nums = input().split(" ")

print(int(nums[0]) + int(nums[1]))
'''

# print(sum(list(map(int, input().split()))))

#print(sum(map(int, input().split())))

#print(sum(map(int,input().split())))

import sys
print(sum(map(int, sys.stdin.readline().split())))


'''
리스트는 굳이 안 만들어줘도 되네 -> 근데 있으나 없으나 시간은 똑같다?
: split 자체가 반환이 list형이기 때문인 듯
-> 아니다, list형이 아닌 map 형식으로 제출되며, 리스트와 비슷한 형식이어서 sum연산이 가능했을 뿐인 듯
map 출력 결과 형식을 좀 알아봐야겠다

나랑 똑같은 코드인데 나보다 빠른 코드가 있길래 무슨 차이인가 했는데
int, input() 과 int,input() 차이었다(공백 차이)
그래서 공백 없애고 다시 돌렸는데, 되려 시간은 늘어났다 왜지...?
'''