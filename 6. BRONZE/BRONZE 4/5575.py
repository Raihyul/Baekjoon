for _ in range(3):
    time_card = list(map(int, input().split()))
    start = time_card[0] * 3600 + time_card[1] * 60 + time_card[2]
    end = time_card[3] * 3600 + time_card[4] * 60 + time_card[5]
    work = end - start
    print(work//3600, (work%3600)//60, (work%60))
