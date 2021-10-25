sent = input()
_sum = 0

for s in sent:
    _sum += int(s)

_sum += (len(sent) - 2)*9

print(_sum)