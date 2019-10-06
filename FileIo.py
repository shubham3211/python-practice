import csv
# f = open('a.txt', 'r')
# print(f.name)
# fc = f.read(1)
# print(f.tell())
# f.seek(0)
# print(f.tell())
# while len(fc)>0:
#   fc = f.read(1)
#   print(fc, end = '*')
# li = f.readlines()
# print(li)
# print(f.readline())

# f2 = open('a1.txt', 'a')
# f.seek(0)
# for l in f:
#   f2.write(l)
#   f2.seek(0)
# print(f.writable())
# f2.close() 
# f.close()

myFile = open('home/shubham/Documents/Untitled1.csv')
mr = csv.reader(myFile)
print(mr)