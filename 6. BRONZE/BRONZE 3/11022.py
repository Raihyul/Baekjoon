import sys

for repeat in range(int(sys.stdin.readline())):
    num1, num2 = map(int, sys.stdin.readline().split())
    sys.stdout.write(f"Case #{repeat+1}: {num1} + {num2} = {num1+num2}\n")