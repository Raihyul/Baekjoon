while True:
    num = input()
    if num == '0':
        break
    else:
        while True:
            if num[0] != num[-1]:
                print("no")
                break
            elif len(num) < 2 or (len(num) == 2 and num[0] == num[1]):
                print("yes")
                break
            else:
                num = num[1:-1]