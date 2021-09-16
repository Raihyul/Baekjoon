sen = input().upper()
sen_dict = {}

for s in sen:
    if s in sen_dict:
        sen_dict[s] += 1
    else:
        sen_dict[s] = 1

max_word = max(sen_dict.values())

if list(sen_dict.values()).count(max_word) > 1:
    print('?')
else:
    for k, v in sen_dict.items():
        if v == max_word:
            print(k)