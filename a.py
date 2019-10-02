l = [5, 6, 2, 5, 3, 3, 6, 5, 5, 6, 5]
print(sorted(set(l), key = lambda x: l.count(x), reverse=True))

l1=[2, 4, 10, 20, 5, 2, 20, 4]

def remove_duplicate(x):
  for k in x:
    if x.count(k)>1:
      x.remove(k)

remove_duplicate(l1)
print(l1)

l2= [[1, 0, -1], [-1, 0, 1], [-1, 0, 1], [1, 2, 3], [3, 4, 1]]
# a = set()
# for i in l2:
#   i.sort()
#   a.add(tuple(i))
# l2 = list(a)
# print(l2)

res = list(set(map(lambda i: tuple(sorted(i)), l2)))

l3 = [[-11, 0, 11], [-11, 11, 0], [-11, 0, 11], [-11, 2, -11], [-11, 2, -11], [-11, -11, 2]]
r = set(map(lambda a : tuple(sorted(a)), l3))
print(r)
