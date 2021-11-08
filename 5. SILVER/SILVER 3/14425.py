from sys import stdin
from collections import Counter
n, m = map(int, stdin.readline().split())
sentences = stdin.readlines()
test = Counter(sentences[n:])
count = 0
for s in sentences[:n]:
    count += test[s]
print(count)

# 검사해야하는 목록에서 집합 S에 속하지 않지만 겹치는 것들이 지워지는 문제 발생
# n = sum(map(int, stdin.readline().split()))
# m = set(stdin.readlines())
# print(n - len(m))