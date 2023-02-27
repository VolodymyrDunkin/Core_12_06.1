# fd = open('test2.txt')
lst = [str(i) for i in range(10)]

with open('test2.txt', 'w') as fd:
    print(fd.writelines(lst))


