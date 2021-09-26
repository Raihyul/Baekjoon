K, D, A = map(int, input().split('/'))
print('hasu' if (K+A<D or D==0) else 'gosu')
# print(['gosu','hasu'][k+a<d or d==0])