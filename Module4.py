import csv
import os
#Question 1
myFile = open('Employee.csv', 'w+')
writing = csv.writer(myFile)
writing.writerow(["EmpCode", "EmpName", "EmpAge", "EmpSalary"])
writing.writerow(["1", "aman", "22", "200"])
writing.writerow(["2", "boy", "21", "2001"])
writing.writerow(["3", "camroon", "20", "202"])
writing.writerow(["4", "duke", "19", "2002"])
writing.writerow(["5", "shubham", "18", "2003"])
myFile.seek(0)
reading = csv.reader(myFile)
mylist = list(reading)
print(mylist)
myFile.close()

# Question 2
os.mkdir('C:\\PythonDir')
os.rename('C:\\PythonDir', "C:\\PythonDirectory")
os.rmdir('C:\\PythonDirectory')