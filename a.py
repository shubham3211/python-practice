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

print(max(len(x) for x in [['A'], ['A', 'B'], ['A', 'B', 'C']] ))

print(max(map(len, [['A'], ['A', 'B'], ['A', 'B', 'C']] )))

k = [1, 3, 4, 3, 6, 7]
k = [ i for i in range(len(k)) if k[i] == 3]
print(k)

arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
res = [x for x in arr if x==0] + [x for x in arr if x == 1]
print(res)

a = "$Gee*k;s..fo, r'Ge^eks?"
p = "".join([x for x in a if x.isalpha()])
print(p)

l = ['gfg', 'i', 's', 'be', 's', 't']
l = [i for x in l for i in x if x.isalpha() == True]
print(l)

a = 'a'
for i in range(26):
  print(a, end='')
  a = chr(ord(a)+1)

n = 100
n = bin(n)
l = [x for x in n if x == '1']
print(len(l))

arr1 = [-1, -2, 4, -6, 5, 7]
arr2 = [6, 3, 4, 0]
l = [(8-i, i) for i in arr1 if 8-i in arr2] 
print(l)

arr = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
f = [x for x in arr if x<14]
m = [x for x in arr if x>14 and x<20]
e = [x for x in arr if x>20]
print(f+m+e)

s = "geeksforgeeks"
l = [x for x in s if s.count(x) == 1]
print(l)

arr = [0, 1, 2, 3, 4, 5, 6, 7]
e = [x for x in range(len(arr)) if x%2 == 0]
o = [x for x in range(len(arr)) if x%2 !=0]
arr = sorted(e) + sorted(o)
print(arr)

def countSetBits(n):
  b = bin(n)
  l1 = [b[i] for i in range(len(b)) if b[i]=='1' ]
  return len(l1)

l = sum(map(countSetBits, [x for x in range(3)]))
print(l)

arr = [1, 2, 0, 4, 3, 0, 5, 0]
arr = [x for x in arr if x != 0] + [x for x in arr if x == 0]
print(arr)

m =[[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1],  [0, 0, 0, 0]]
print(max(map(lambda a: a.count(1), m)))

l = [10, 20, 10, 30, 40, 40]
l = [x for x in l if l.count(x) == 1]
print(l)

a = set((1, 2, 3))
b = set((3, 4, 5))
print(a&b)

l1 = [10, 15, 20, 25, 30, 35, 40]
l2 = [25, 40, 35]
l1 = set(l1)
l2 = set(l2)
l1 = list(l1 - l2)
print(l1)

a = [3, 4, 1, 3, 4, 5]
print(a.index(max(a))+1)
print(a.index(min(a))+1)

def multiple(n, m):
  a = range(n, (m*n)+1, n)
  print(*a)

multiple(3, 5)

l = [1, 2, 3]
a = []
for i in range(len(l)):
  for j in range(len(l)):
    if j>=i:
      a.append(l[i:j+1])
print(a)

#sort the list according to length
l = ["rohan", "amy", "sapna", "muhammad", "aakash", "raunak", "chinmoy"]
print(sorted(l, key = len))

l = [10, 20, 30, 40, 50, 60, 70, 80, 90]
i = 0

c = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"]
d = {}
for i in c:
  if i in d:
    d[i] = d[i] + 1
  else:
    d[i] = 1
print(d)

a1 = [1, 5, 10, 20, 40, 80]
a2 = [6, 7, 20, 80, 100]
a3 = [3, 4, 15, 20, 30, 70, 80, 120]

d.clear()

a = {}
b = {}
c = {}

for i in a1:
  a[i] = 1
for i in a2:
  b[i] = 1
for i in a3:
  c[i] = 1
print(a.keys() & b.keys() & c.keys())

a = 8
b = 4
b1 = bin(a)
b2 = bin(b)
d1 = {}
d2 = {}
for i in b1:
  if i in d1:
    d1[i] = d1[i]+1
  else:
    d1[i] = 1
for i in b2:
  if i in d2:
    d2[i] = d2[i]+1
  else:
    d2[i] = 1
if d1['1']==d2['1'] and d1['0']==d2['0']:
  print("Yes")
else:
  print("No")

s = "ant magenta magnate tan gnamate"
w = s.split(" ")
# for i in range(len(w)):
#   w[i] = "".join(sorted(w[i]))
d.clear()
d = {}
for i in w:
  k = "".join(sorted(i))
  if i in d:
    d[k] = (i, d[i]+1)
  else:
    d[k]= (i, 1)
print(d)

a = ['cat', 'dog', 'tac', 'god', 'act']
d = {}
for i in a:
  k = "".join(sorted(i))
  if k in d:
    d[k].append(i)
  else:
    d[k] = []
print(d)
d.clear()

k = "hello"
for i in k:
  if i in d:
    d[i] = d[i]+1
  else:
    d[i] = 1

l = []
for i in d:
  if d[i] == 1:
    l.append(i)
for i in l:
  del d[i]
print(d) 

a = "abcdefghijklmnopqrstuvwxyz"
s = "paradox"
s = list(s)
for i  in range(len(s)):
  k = a.index(s[i])
  s[i] = a[-k-1]
print(s)

s1 = "ABHISHEKsinGH"
s2 = "gfhfBHkooIHnfndSHEKsiAnG"

d1 = {}
d2 = {}
a = set()
b = set()
for i  in s1:
  a.add(i)
for i in s2:
  b.add(i)
if a&b == a:
  print("Yes")

for i in d.items():
  print(i)

l = [{ "name" : "Nandini", "age" : 20},  { "name" : "Manjeet", "age" : 20 }, { "name" : "Nikhil" , "age" : 19 }] 
l = sorted(l, key=lambda x: x["age"], reverse = True)
print(l)