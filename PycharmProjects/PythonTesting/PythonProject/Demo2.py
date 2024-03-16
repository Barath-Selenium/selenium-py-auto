values = [1, 2, "Barath", 4, 5]

print(values[0])
print(values[1])
print(values[2])
print(values[3])
print(values[-1])  # printing last values in list.
print(values[1:5])
values.insert(3, "krsna")  # inserting values in list
values.append("hare hare")  # add values in end of the list that why using append.
print(values)

values[2] = "BARATH"  # Update values in list

print(values)

del values[0]
print(values)


tup = (1, 2, "its tuple so its immutable", 4)
print(tup)
print(tup[2])

# Dictionary

dic = {1: "a", "b": 2, "c": "Hello Wrld"}
print(dic)


dict = {}

dict[1] = "a"
dict["FirstName"] = "Barath"
dict["LastName"] = "Krsna"
print(dict)
print(dict[1])





