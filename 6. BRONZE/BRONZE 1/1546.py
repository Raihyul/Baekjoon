input()
score = list(map(int, input().split()))
print(sum(score)/len(score)/max(score)*100)