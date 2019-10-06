# c = 10
# def m():
#   c = 20
# c = 10
# m()
# print(c)

# s = "I love Geeksforgeeks" 
# def f():
#   print(s)
#   s = "Me too."
#   print(s)
# f() 
# print(s) 

l1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
l2 = list(filter(lambda x: x%2!=0, l1))
l3 = list(map(lambda x, y: x+y, l1, l2))
print(l3)

def g():
  '''l,cld,scl;ds,c;d'''
  x=10

print(g.__doc__)
