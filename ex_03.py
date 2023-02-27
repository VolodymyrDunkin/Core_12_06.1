fd = open('test2.txt')
data = fd.read().split('\n')
print(fd.closed)
fd.close()
print(fd.closed)

print(type(data))

# for ch in data:
#     print(ch)

fd = open('test2.txt')
data = fd.readlines()
fd.close()

print(data)

fd = open('test2.txt')
# line = fd.readline()
# while line:
#     print(line)
#     line = fd.readline()
# # data = fd.readline()
fd.close()

# print(data)

fd = open('test2.txt')
line = fd.readline()
print(line)
print(f'position - {fd.tell()}')
line = fd.readline()
print(line)
print(f'position - {fd.tell()}')
# while line:
#     print(line)
#     line = fd.readline()
# # data = fd.readline()
fd.close()