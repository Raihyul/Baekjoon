for _ in range(int(input())):
    cnt, sen = input().split()
    for word in sen:
        print(word*int(cnt), end='')
    print()