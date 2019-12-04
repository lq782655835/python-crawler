# -*- coding: UTF-8 -*-
import os

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
    print({3, 1, 2, 1}) #set([1, 2, 3]) set的快捷方式
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
    path = '%s/practice/helloworld.py' % os.getcwd()
    print(path)
    # f = open(path)
    # print(f.read())
    # f.close()
    # 等价于
    with open(path) as f:
        print(f.read())

def myComprehension():
    list1 = range(10)
    print([ index + item for index, item in enumerate(list1)]) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    print([x * 2 for x in list1]) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

def myDict():
    dict1 = { 'a': 1, 'b': 2}
    for key in dict1: print(key, dict1[key])

def myGlobalLen():
    print(len('hello')) # 5
    # print(len((1, 2)) # invalid syntax
    print(len([1, 2])) # 2
    print(len({'a': 1, 'b': 2})) # 2
    print(len(set([1,2,1,3]))) # 3

def myGlobalList():
    print(list('hello')) # ['h', 'e', 'l', 'l', 'o']
    print(list({'a': 1, 'b': 2})) # ['a', 'b']
    # print(list((2, 4)) # invalid syntax
    # print(list(set([1,2,1,3]))) # invalid syntax

def myGlobalEnumerate():
    for index, val in enumerate('hello'): print(index, val) # (0, 'h') (1, 'e')...
    for index, val in enumerate([1, 2]): print(index, val) # (0, 1) (1, 2)
    for index, val in enumerate((1, 2)): print(index, val) # (0, 1) (1, 2)
    for index, val in enumerate(set([1,2,1,3])): print(index, val) # (0, 1)(1, 2)(2, 3)

# myList()
# myTuple()
# mySet()
# myString()
# myFile()
# myComprehension()
# myDict()

# myGlobalLen()
# myGlobalList()
# myGlobalEnumerate()


class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

# class ChinaBankAccount(BankAccount):
#     def __init__(self, name):
#         self

bank = BankAccount()
bank.deposit(100)
bank.withdraw(20)
print(bank.balance) # 80
