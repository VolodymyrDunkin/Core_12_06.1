def count_ch(word, lst=[]):
    print(lst)
    lst = []
    lst.append(word)
    lst.append(len(word))
    return lst


if __name__ == "__main__":
    print(count_ch('Hello', [1, 2, 3, 4]))
    print(count_ch('World'))