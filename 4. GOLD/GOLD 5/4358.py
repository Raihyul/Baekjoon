from sys import stdin, stdout
from collections import Counter
trees = Counter(stdin.readlines())
total = sum(trees.values())
for tree in sorted(trees.items()):
    print(tree[0].rstrip(), round(tree[1]/total*100, 4))
    # stdout.write(tree[0][:-2] + " " + str(round(tree[1]/total*100, 4)) + '\n')