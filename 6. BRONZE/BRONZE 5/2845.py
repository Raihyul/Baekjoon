L, P = map(int, input().split())
print(*[int(x) - L*P for x in list(input().split())])


# gaps = [int(x) - L*P for x in list(input().split())]
# for gap in gaps:
#     print(gap, end=' ')