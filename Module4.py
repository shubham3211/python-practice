import csv
import os
#Question 1
myFile = open('Employee.csv')
reading = csv.reader(myFile)
mylist = list(reading)
print(mylist)
myFile.close()

#Question 2
os.mkdir('C:\\PythonDir')
os.rename('C:\\PythonDir', "C:\\PythonDirectory")
os.rmdir('C:\\PythonDirectory')