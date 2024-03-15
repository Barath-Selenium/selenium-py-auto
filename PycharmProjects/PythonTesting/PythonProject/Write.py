# with open('test.txt', 'r') as reader:
#     content = reader.readlines()
#     reversed(content)
#     with open('test.txt', 'w') as writer:
#         for line in reversed(content):
#             writer.write(line)
#

with open('test.txt', 'r') as reader:
    content = reversed(reader.readlines())

with open('test.txt', 'w') as writer:
    writer.writelines(content)



