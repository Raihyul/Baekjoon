_sum = 0
for _ in range(5):
    score = int(input())
    _sum += score if score>=40 else 40
print(_sum//5)