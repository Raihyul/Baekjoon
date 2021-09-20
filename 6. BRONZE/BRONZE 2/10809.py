s = input()
i = 0
_dict = {}

for word in s:
    if word not in _dict.keys():
        _dict[word] = i
    i += 1

for alphabet in 'abcdefghijklmnopqrstuvwxyz':
    try:
        print(_dict[alphabet], end=' ')
    except:
        print(-1, end=' ')