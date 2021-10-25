n = int(input())
fibo = [0, 1]

if n <= 1:
    print(fibo[n])
else:
    for i in range(n-1):
        fibo.append(fibo[-1] + fibo[-2])
    print(fibo[-1])