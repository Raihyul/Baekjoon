import math
D, H, W = map(int, input().split())
ratio = math.sqrt(D**2 / (H**2 + W**2))
print(math.floor(H*ratio), math.floor(W*ratio))