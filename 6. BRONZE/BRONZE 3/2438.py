import sys

floor = int(sys.stdin.readline())

for repeat in range(floor):
    sys.stdout.write(f"{' '*(floor-repeat-1)}{'*'*(repeat+1)}\n")