import sys

for num in range(int(sys.stdin.readline())):
    sys.stdout.write("Case #" + str(num+1) + ": " + str(sum(map(int, sys.stdin.readline().split()))) + '\n')