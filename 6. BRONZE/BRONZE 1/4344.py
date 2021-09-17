for _ in range(int(input())):
    _list = list(map(int, input().split()))
    _avg = sum(_list[1:])/_list[0]
    cnt = 0
    for score in _list[1:]:
        if score > _avg:
            cnt += 1
    print(f"{cnt/_list[0]*100:.3f}%")