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

l4 = [1, 5, 3, 6, 3, 5, 6, 1]
l4 = list(set(l4))
print(l4)

#swap the first and last element of the list
l5 = [12, 35, 9, 56, 24] 
g = l5[0], l5[-1]
l5[-1], l5[0] = g
print(l5)

start, *middle, last = l5
l5 = [last, *middle, start]
print(l5)

e = l5.pop()
b = l5[0]
l5.append(b)
l5[0] = e
print(l5)

def swapPosition(l, p1, p2):
  l[p1], l[p2] = l[p2], l[p1]
  print(l)

swapPosition(l5, 1, 2)

def removeIthWord(l, word, n):
  c = 0
  for i in range(len(l)):
    if l[i] == word:
      c+=1
      if c == n:
        del l[i]
  print(l)

removeIthWord(['geeks', 'for', 'geeks'], 'geeks', 2)