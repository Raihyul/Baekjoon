for _ in range(int(input())):
    score = 0
    con = 0
    for ans in input():
        if ans == "O":
            con += 1
            score += con
        else:
            con = 0
    print(score)