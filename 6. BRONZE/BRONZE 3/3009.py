x, y = [], []
for _ in range(3):
    temp_x, temp_y = map(int, input().split())
    x.append(temp_x) if temp_x not in x else x.remove(temp_x)
    y.append(temp_y) if temp_y not in y else y.remove(temp_y)
print(*x, *y)