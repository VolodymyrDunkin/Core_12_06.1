# file = open('test.txt')
# print(file.read())
# file.close()


# fd = open('test1.txt', 'x')
# print(fd.read())
# fd.close()

# fd = open('test2.txt', 'w')
# fd.write('Hello World')
# fd.close()

# fd = open(r"D:\New folder (2)\New folder\mydoc.txt")
# print(fd.read())
# fd.close()

# fd = open('test3.txt', 'x')
# fd.close()

fd = open('test1.txt', 'w')
fd.write('Hello from python')
fd.close()

fd = open('test1.txt', 'a')
fd.write('Hello from python')
fd.close()


fd = open('test1.txt', 'w+')
fd.write('Llsdjlfjlks')
print(fd.seek(5))
print(fd.read())
fd.close()