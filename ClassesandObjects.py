import os
import csv
from sys import argv
class Computer:
  ram  =10
  def __init__(self):
    self.i=0
    self.k1 = self.keyboard()
    self.ram=30

  def config(self):
    self.i=10

  @classmethod
  def info(cls):
    return cls.ram

  @staticmethod
  def sm():
    print("I am in a static method")
  
  class keyboard:
    def __init__(self):
      self.keys = 100
      self.color = 'black'

c1 = Computer()
c2 = Computer()
print(type(c1))
Computer.config(c1)
print(c1.i)
print(c2.i)
print(__file__)
print(__name__)
a = []
print(id(a))
print(Computer.ram)
Computer.ram = 100
print(c1.ram)
print(c2.ram)
print(Computer.info())
print(Computer.sm())
print(c1.k1.color)
print(c1.__dict__)
c5 = Computer()
print(c5.__dict__)
print(type(c5.k1))
print(type(c5))
k = c5.k1
print(k.__dict__)
k.color = "green"

# class A:
#   name = "parth"
#   def __init__(self):
#     print("In a")
#     self.name = "shubham"
#     self.age = 22
#   def _printHi(self):
#     print("Hi")
  # def getName(self):
  #   return self.name

# class B(A):
  # def __init__(self):
  #   print("In b")
  #   super().__init__("shubham")
  #   print(super().printHi())
  #   print(self.printHi())
#   def a(self):
#     print(self.name, self.age)
#     self._printHi()
  
# b1 = B()
# b1.a()
# b1.printHi()
# print(b1.getName())

# class C:
#   def func1(self):
#     print("In c")

# class D(C):
#   def func1(self):
#     print("In d")

# def p(name=None, age=None):
#   print(name, age)

# def p(name, age, height):
#   print(name, age, height)

s = "My name is\n shubham"
print(s)

d = dict(foo='x', bar='y', baz='z')
print("foo is {foo} bar is {foo} baz is {baz}".format(foo=2, baz=3, p=2))

print(3.3 +4)

a =5
b=10
print(a.__sub__(10))
print(a)

class alpha:
  def __init__(self, a):
    self.a = a
    self.__b =5
  def __add__(self, o):
    return self.a + o.a
  def __sub__(self, o):
    return self.a - o.a
  def __mul__(self, o):
    return self.a*o.a
  def __truediv__(self, o):
    return self.a/o.a
  def __mod__(self, o):
    return self.a/o.a
  def __pow__(self, o):
    return self.a**o.a
  def __floordiv__(self, o):
    return self.a//o.a
  def __radd__(self, o):
    return self.a + o.a
  def __lt__(self, o):
    return self.a<o.a
  def __gt__(self, o):
    return self.a>o.a
  def __le__(self, o):
    return self.a<=o.a
  def __ge__(self, o):
    return self.a>=o.a
  def __eq__(self, o):
    return self.a == o.a
  def __ne__(self, o):
    return self.a!=o.a
  def __iadd__(self, o):
    self.a+=o.a
  def __isub__(self, o):
    self.a-=o.a
  def __imul__(self, o):
    self.a*=o.a
  def __idiv__(self, o):
    self.a/=o.a
  def __ifloor__(self, o):
    self.a//=o.a
  def __imod__(self, o):
    self.a%=o.a
  def __ipow__(self, o):
    self.a**=o.a
  def __neg__(self):
    # self.a = -self.a
    return -1*self.a
  def __getitem__(self, index):
    return 5
  def __contains__(self, val):
    return True
  def __len__(self):
    return 4
  def __str__(self):
    return str(self.a)
a1 = alpha(4)
a2 = alpha(5)
print(a1+a2)
class beta:
  def __init__(self, a):
    self.a = a
a3 = beta(4)
print(a3 + a1)
d = {}
d.update({"name": "shubham", "age": 22})
print(d)
print(a1+a2, a1*a2, a1/a2, a1**a2, a1<a2, a1>a2, a1>=a2, a1==a2, a1//a2)

print(r"shubham is \x msmkl")


class A1:
  pass
class B1:
  pass
class A2:
  pass
class B2:
  pass
class C1(A1, B1):
  pass
class D1(A2, B2):
  pass
class E1(C1, D1):
  pass
print(E1.__mro__)

l = [1, 2, 3, 4 ]
print(l.pop())
print(l)

l = {1, 2, 3, 4, "0"}
print(l.pop())
print(l)

d = {"a": 1 , "b": 2}
d.popitem()
print(d)

class O:
  ''' first doc string'''
  def __init__(self):
    pass
  '''second doc string'''
k = O()
print(k.__doc__)
print(a1[-1])
print(a1)
print(len(a1))
print(2 in a1)
del a1
l = [1, 2, 3, 4, 5]
p = tuple(l)
print(p)

l = [1, 2, 3, 4]
r = map(lambda x : x*x, l)
print(list(r))

class Complex:
  c = 0
  def __init__(self, r, i):
    self.r = r
    self.i = i
    print(self.c)
    Complex.c = Complex.c + 1
    # self.inc()
  # @classmethod
  # def inc(cls):
  #   c = c+1
  def __mul__(self, o):
    r = self.r*o.r
    i = self.i*o.i
    return Complex(r, i)
  def __eq__(self, o):
    if self.i == o.i and self.r == o.r:
      return True
    return False

c1 = Complex(1, 1)
c2 = Complex(2, 3)
print(Complex.c)
print('''
;lwd;qwd;lq,d
d,l;,ed;l,e
ldl,ed;l,d
''')
k = l*3
l.extend(k)
m = [100, 300, 400]
l.extend(m)
print(l)

# l = list()
# p = tuple(1)
s = set({"1",2 , 3})
d = dict(x=5, y=10)
k = dict.fromkeys(('1', '2', '3'), 0)
t = tuple((1, 2, 3))
print(d, k)
print(l)
f = [0, 1, 2]
# map(lambda x: f.append(sum(f[-2:])), [1, 1, 1, 1, 1, 1, 1])
print(f)
m = [(1, 2), (3, 4)]
d = dict(m)
print(d)
del d[1]
t = (1, 2, 3, [1, 2, 3])
print(t)
t = 1, 2, 3, "hello world"
print(t)
setA = {1, 2, 3, 4}
steB = {5, 6, 7, 8}
print(setA | steB)
l = [1, 2, 3, 4]
t = tuple(l[-3:])
print(t)
l.reverse()
print(l)
print(d)
d = {"a": 4}
print(d.pop("a"))

f = open('l.txt', 'r')
# f.write('mlkemklemf')
# f.seek(0)
print(f.tell())
# k = f.read()
# print(k)
# for i in f:
#   print(i)
# f.write("ac;")
# print(f.writable())
# l = ["1", "2", "3", "4", "5"]
# # f.writelines(l)
# k = f.read()
# print(type(k))
# p = k.split(" ")
# f1 = open('abc.txt', 'r')
# # for i in p:
# #   f1.write(i+'\n')
# j = 0
# i = f1.readline()
# while len(i)>0:
#   print(i)
#   i = f1.readline()
# f1.seek(0)
# f.close()
# f1.close()
# print(f.name)
# print(f.closed)
# with open('abc.txt') as f:
#    k = f.read()
#    print(k.find("hd,;lq"))
# with open('k.csv', 'w'  ) as f:
#   w = csv.writer(f)
#   w.writerow(['name', 'age', 'path'])
#   w.writerow(['name', 'age', 'path'])

# with open('k.csv', 'r+') as f:
  # r = csv.reader(f)
  # w = csv.writer(f)
  # data = list(r)
  # print(data)
  # for i in data:
  #   w.writerow(i+['shubham'])
  # w.writerow(['1', '2', '3'])

# print(os.getcwd())
# os.mkdir('./hello/world/p')
# os.rmdir('./hello')
# os.system('date')
# print(os.stat('./'))
# os.makedirs('./hello/world/a/b/c/d')
# os.removedirs('./hello')
# os.rename('./hello', './bye')
# print(os.listdir())
# os.unlink('abc.txt')
print(os.uname())

# class spg:
#   def __init__(self):
#     self.a = 10
#     self.x =100
#   def __del__(self):
#     print("Object deleted")
# a = spg()
# print(hasattr(a, 'a'))
# del a.a
# delattr(a, 'a')
# del a.x
# print(a.__dict__)
# del a
# print(hasattr(a, 'a'))

# class A:
#   def __init__(self, b):
#     self.b = b
#   def __del__(self):
#     print("A deleted")

# class B:
#   def __init__(self):
#     self.a = A(self)
#   def __del__(self):
#     print("B  deleted")

# print(argv)
# args = [int(x) for x in argv[1:] if int(x) != 10]
# print(sum(args))

l = [1, 2, 3]
l1, l2, l3 = l
print(l1, l2, l3)

# a, b = [int(x) for x in input("Enter 2 numbers").split(" ")]
# print(a, b)
# s = ["Shuisham", "is", "A", "Goodi", "Boy"]
# s = " ".join(s)
# k = "   "
# print(s)
# print(s.zfill(100))

f = 0
s = 1
print(f)
print(s)
# for i in range(10):
#   t = f+s
#   print(t)
#   f = s
#   s = t
f = [0, 1]
a = 10
b = 0
try:
  print("resource open")
  print(a/b)
  k = int(input("Enter a number"))
  print(k)
except ZeroDivisionError as z:
  print("Division by  zero not allowed", z)
except ValueError as v:
  print("Value not valid", v)
except Exception as e:
  print("Exception occoured", e)
finally:
  print("Done")
print("Do anything even if error occured")

f = open('b.txt')
l = [x.rstrip() for x in f]
print(l)
f.close()

def my_function(*p, **k):
    print(k)

my_function(1, 2, 3, 4, a=12, b="abc")

d = dict(a=10, b=12)
print(d)

def r1(a, b=1, c=2):
  print(a, b, c)

r1(1, c=3)

l = [1, 2, 3, 4, 5, 6, 7]
l1 = list(map(lambda x: x**x, l))
l2 = list(filter(lambda x: x%2 == 0, l))
print(l1, l2)

a = (1, 2, 3, 4)
x, y, *z = a
l = [1, 2, 3, 4]
print(*l)