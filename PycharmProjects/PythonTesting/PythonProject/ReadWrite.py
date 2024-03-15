file = open('test.txt')
# to read all the line in the file             print(file.read())
# to read the line based on provided index     print(file.read(4))
# to read the single line in file              print(file.readline())


# line = file.readline()
# while line != "":
#     if line.strip():
#         print(line.strip())
#         line = file.readline()


for line in file.readlines():
    if line.strip():
        print(line.strip())

file.close()










