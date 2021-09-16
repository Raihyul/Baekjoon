hexa = input()[::-1]

hexa_dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

octa = 0

for i in range(len(hexa)):
    if hexa[i] in hexa_dict:
        octa += hexa_dict[hexa[i]] * (16**i)
    else:
        octa += int(hexa[i]) * (16**i)

print(octa)