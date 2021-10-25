angle = []

for _ in range(3):
    angle.append(int(input()))

if sum(angle) != 180:
    print("Error")
else:
    count = len(set(angle))
    if count == 1:
        print("Equilateral")
    elif count == 2:
        print("Isosceles")
    else:
        print("Scalene")