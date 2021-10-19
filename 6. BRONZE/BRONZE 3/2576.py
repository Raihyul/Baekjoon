_list = []
for _ in range(7):
    num = int(input())
    if num % 2 == 1:
        _list.append(num)
if len(_list) > 0:
    print(sum(_list))
    print(min(_list))
else:
    print(-1)