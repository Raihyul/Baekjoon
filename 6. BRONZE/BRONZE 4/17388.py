participation = list(map(int, input().split()))

if sum(participation) >= 100:
    print("OK")
else:
    print(["Soongsil", "Korea", "Hanyang"][participation.index(min(participation))])