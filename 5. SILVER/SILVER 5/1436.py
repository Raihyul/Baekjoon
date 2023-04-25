'''
# 1436. 영화감독 숍
import sys

cnt = 0
num = 666
series = int(sys.stdin.readline())

while cnt < series:
    if '666' in str(num):
        cnt += 1
    
    num += 1

print(num-1)
'''

#print([i for i in range(9**7)if"666"in str(i)][int(input())-1])
import sys

sys.setrecursionlimit(10**6)

N = int(input())
movie_title = 666

def checkMovieTitle(N,movie_title):
    if "666" in str(movie_title): # 666이 들어간 숫자인 경우
        N -= 1
        if N == 0: # 출력해야하는 숫자
            return print(movie_title)
        else: # 이전 시리즈의 숫자
            checkMovieTitle(N, movie_title + 1)
    else: # 666이 없는 숫자인 경우
        checkMovieTitle(N,movie_title + 1)

checkMovieTitle(N,movie_title)