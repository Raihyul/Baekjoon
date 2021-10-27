value = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}

color1 = input()
color2 = input()
color3 = input()

print((value[color1] * 10 + value[color2]) * (10 ** value[color3]))

colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
print((10*colors.index(input()) + colors.index(input())) * 10**colors.index(input()))