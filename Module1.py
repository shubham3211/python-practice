#Activity 1
#Question 4
# def printHello():
#   print("hello")

#Question 5
string = "All work and no play make Jack a dull boy"
strList = string.split(" ")
print(" ".join(strList))

#Activity 2
#Question 1
print(5%2)
print(9%5)
print(15%12)
print(12%15)
print(0%7)
# print(7%0)

x = int(input("Enter x"))
y = int(input("Enter y"))

if x<y:
  print(x, "is less than", y)
elif y<x:
  print(x, "is greater than ", y)
else:
  print(x, "is equal to ", y)

#Question 3
print(True or False)
print(True and False)
print(not(True) and False)
print(True or 7)
print(False or 7)
print(True and 0)
print(False or 8)
print("happy" and "sad")
print("happy" or "sad")
print("" and "sad")
print("happy" and "")

#Activity 3
#Question 1
i = 1
while i<=25:
  if i%2==0:
    print(i)
  i = i+1

for i in range(1, 26):
  if i%2 == 0:
    print(i)

n = int(input("Enter number to find factorial"))
i = 1
ans = 1
while i<=n:
  ans = ans*i
  i = i+1

print(ans)

#Activity 4
#Question 1
def sum_of_squares(num):
  s = 0
  while num!=0 :
    s = int(num%10) ** 2 + s
    num = num//10
  return s

print(sum_of_squares(987))