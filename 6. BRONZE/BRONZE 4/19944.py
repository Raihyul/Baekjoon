n, m = map(int, input().split())

if m < 3:
    print('NEWBIE!')
elif m < n+1:
    print('OLDBIE!')
else:
    print('TLE!')