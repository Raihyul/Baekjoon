while True:
    l = list(map(int, input().split()))
    if sum(l) == 0:
        break
    d = max(l)
    l.remove(d)
    if l[0]**2 + l[1]**2 == d**2:
        print("right")
    else:
        print("wrong")