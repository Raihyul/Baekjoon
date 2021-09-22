dices = list(map(int, input().split()))
dices_set = set(dices)
dice_dict = {}

for dice in dices_set:
    dice_dict[dices.count(dice)] = dice

if max(dice_dict.keys()) == 3:
    print(10000 + dice_dict[3]*1000)
elif max(dice_dict.keys()) == 2:
    print(1000 + dice_dict[2]*100)
else:
    print(max(dices)*100)


'''
a,b,c=sorted(map(int,input().split()))
print([c,b+10,b*10+100][[a,b,c].count(b)-1]*100)
'''