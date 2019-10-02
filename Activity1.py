l=[101, 201, 301, 401]
l.append(101)
print(l)
l=l+[601]
print(l)
l.insert(3, 777)
print(l)
for i in l:
  print(i)
v1, v2, v3 = l[:3]
t=tuple(l[-3:])
print(t)

  
