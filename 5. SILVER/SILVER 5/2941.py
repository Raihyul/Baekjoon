words = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

sentence = input()
count = 0

for word in words:
    count += sentence.count(word)

print(len(sentence) - count)