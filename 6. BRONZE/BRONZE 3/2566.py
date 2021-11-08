numbers = []
indexes = []

for _ in range(9):
    _list = list(map(int, input().split()))
    numbers.append(max(_list))
    indexes.append(_list.index(max(_list)))

print(max(numbers))
print(numbers.index(max(numbers))+1, indexes[numbers.index(max(numbers))]+1)