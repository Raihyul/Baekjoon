# 2750. 수 정렬하기
'''
import sys

N  = int(sys.stdin.readline())
_list = []

for i in range(N):
    _list.append(int(sys.stdin.readline()))

_list.sort()

#for num in _list:
#    print(num)

print(*_list, sep='\n')
'''
import sys

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

N  = int(sys.stdin.readline())
_list = []

for i in range(N):
    _list.append(int(sys.stdin.readline()))

print(*quick_sort(_list), sep='\n')