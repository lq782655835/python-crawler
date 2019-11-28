# -*- coding: UTF-8 -*-

def myList():
    list1 = [0, 1, 2, 3, 4]
    list2 = [1, 2, 3]
    print(len(list1), list1[0]) # (5, 0)
    print(list1[1:2]) # [1]
    print(range(4), range(1, 4)) # ([0, 1, 2, 3], [1, 2, 3])
    print(zip(list1, list2)) # [(0, 1), (1, 2), (2, 3)]
    print(list1.append(5)) # None

    for i in list1:
        print(i)
    for l1, l2 in zip(list1, list2):
        print(l1, l2)

def myTuple():
    t = 2, 3, 4
    print(len(t), t[0]) # (3, 2)
    return 6, 7

def mySet():
    s = set([3, 1, 2, 1])
    print(len(s), s) # (3, set([1, 2, 3])) # Error s[0]: 'set' object does not support indexing
    print(s.add(4)) # None
    print(5 in s) # False
    for i in s:
        print(i) # 1, 2, 3, 4

def myString():
    s = 'hello world'
    print(s[-2], s[1: 5]) # ('l', 'ello')
    formatStr = 'hello %s' % 'word'
    print(formatStr)

def myFile():
    path = '/Users/liaoqiao/netease/lq782655835/python-crawler/practice/hello_package.py'
    # f = open(path)
    # print(f.read())
    # f.close()
    with open(path) as f:
        print(f.read())

# myList()
# myTuple()
# mySet()
# myString()
# myFile()