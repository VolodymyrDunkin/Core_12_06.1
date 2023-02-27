lst = [str(i) for i in range(10)]

fd = open('test2.txt', 'w')

# for i in lst:
#     fd.write(str(i) + '\n')

# fd.writelines(lst)
fd.write('\n'.join(lst))

fd.close()

fd = open('test2.txt', 'a')
fd.write('\n'.join(lst))
fd.close()