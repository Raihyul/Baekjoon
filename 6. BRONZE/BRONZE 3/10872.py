'''
10872. 팩토리얼

0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
'''

def pac(n):
    return 1 if n<=1 else n*pac(n-1)

print(pac(int(input())))