# with open('1-1.png', 'rb') as fd:
#     data = fd.read()

# print(len(data))


with open('Хор - Державний Гімн України.mp3', 'rb') as fd:
    data = fd.read()

bytearray = data[:31]

print(bytearray.decode('utf-8'))