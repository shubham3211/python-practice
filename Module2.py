#Activity 1
myList = [101, 201, 301, 401]
#Question1
myList.append(501)
#Question2
myList = myList + [601]
#Question3
myList.insert(2, 777)
#Question 4
for i in myList:
  print(i)
#Question 5
v1, v2, v3, *v4 = myList
#Question 6
t = tuple(myList[-3:])

#Activity2
batches = {"Java": 34, "SAP": 25, "Testing": 30, "SOA": 22}
#Question 1
keys = batches.keys()
print(keys)
#Question 2
for i in batches:
  print(batches[i])
#Question 3
for i in batches:
  print(batches.get(i))
