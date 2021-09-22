input()
sen = input()

for i in 'JAV':
    sen = sen.replace(i, '')

print(sen if sen else 'nojava')

'''
if len(sen) == 0:
    print('nojava')
else:
    print(sen)
'''