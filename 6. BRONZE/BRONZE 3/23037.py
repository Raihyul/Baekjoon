sum = 0
for num in input():
    sum += int(num)**5
print(sum)

'''
print(sum(map(lambda x: int(x) ** 5, input())))
모두 같은 함수를 적용해야 한다는 점에서 map에 lambda를 사용할 수도 있음
'''