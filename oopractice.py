
######################################################
class SerialGenerator:
    """Machine to create unique incrementing serial numbers. 2 methods"""
    def __init__(self, start=0):
        if not isinstance(start, int):
            raise ValueError("Not an integer")
        self.start = start
        self.value = start

    def generate(self):
        self.value += 1
        return self.value

    def reset(self):
        self.value = self.start

serial = SerialGenerator(start=1000)
serial.reset()
serial.generate()
serial = SerialGenerator(start=4.3)
serial = SerialGenerator(start="hi")

######################################################
import os
import random

class WordFinder:
    _FILEPATH = os.path.join(os.curdir,"ignoreland","words.txt")
    _SEED = 8675309

    def __init__(self, filepath=_FILEPATH):
        file = open(filepath)
        # self.wordlist = file.read(500000).split("\n")
        self.wordlist = self.getwords(file)  # alternatively
        print(str(len(self.wordlist)) + " words read")

    def getwords(self, file):
        wordlist = file.read(500000).split("\n")
        return wordlist

    def random(self):
        return random.choice(self.wordlist)

wf = WordFinder()
wf.random()

class SpecialWordFinder(WordFinder):
    def getwords(self, file):
        wordlist = super(SpecialWordFinder, self).getwords(file)
        wordlist = [w.strip() for w in wordlist if w.strip() and not w.lower().startswith("b")]
        return wordlist

swf = SpecialWordFinder()
swf.random()
###########################################
# https://www.springboard.com/workshops/data-engineering-career-track/learn#/curriculum/24177
# Linked list.
# Insertion/deletion at beginning is O(1); end is O(n).  Linked list does not require preallocation.
# Traversing and accessing are O(n).  Doubly-linked list has link of next and last.
# array indexing is O(1).

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("linkedlist is empty")
            return
        itr = self.head
        llstr = ""

        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data,None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index==0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

# if __name__ == "__main__":
ll = LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(89)
ll.insert_at_end(1)
ll.insert_at_end(9876)
ll.insert_values(["banana","raspberry","mango","grapes","apple","orange"])
ll.get_length()
ll.print()
ll.remove_at(2)
# exercise
# https://github.com/codebasics/data-structures-algorithms-python/tree/master/data_structures/3_LinkedList
######################################################
# Arrays. Lookup, insert, delete are all O(n).
# Python arrays are dynamic arrays.
######################################################
# Memory vs storage
#
######################################################
# stacks
from collections import deque
stack = deque()
# stack.__dir__()
stack.append("cnn.com")
stack.append("cnn.com/world")
stack.append("cnn.com/india")
stack.append("cnn.com/china")
stack
stack.pop()  #  alters the stack and returns the item.
stack
###
# Implement Stack class
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        """reveal next item to be popped"""
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

s = Stack()
s.push(5)
s.is_empty()
############################################
# queue
from collections import deque
q = deque()
q.appendleft(5)
q.appendleft(8)
q.appendleft(27)
q
## Create the class

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

# https://www.hackerrank.com/challenges/equal-stacks/problem
import numpy as np
from operator import itemgetter
from functools import reduce
from itertools import accumulate
import operator
h1 = [3, 2, 1, 1, 1]
h2 = [4, 3, 2]
h3 = [1, 1, 4, 1]
heights1, heights2, heights3 = map(np.array, (h1, h2, h3))
rc_heights1, rc_heights2, rc_heights3 = map(lambda x: list(np.cumsum(x)[::-1]), (heights1, heights2, heights3))
rch_set = list(map(set, (rc_heights1, rc_heights2, rc_heights3)))
intersection = reduce(set.intersection,rch_set)
result = max(intersection)


heights1, heights2, heights3 = h1, h2, h3
rc_heights1, rc_heights2, rc_heights3 = map(lambda x: list(accumulate(x[::-1], func=operator.add))[::-1], (heights1, heights2, heights3))
rch_set = list(map(set, (rc_heights1, rc_heights2, rc_heights3)))
intersection = reduce(set.intersection,rch_set)
result = max(intersection)
return result


###########################################
# https://www.springboard.com/workshops/data-engineering-career-track/learn#/curriculum/24213
# BFS
# neighbor relationships as a list of lists;
# nodes as a dict.
h3 = [1, 1, 4, 1]
h3.append(2)
h3

##########################################
# https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
#
from collections import deque
myqueue = deque()
nops = int(input())
14
n = 0
while n < nops:
    n += 1
    inputhere = input()
    if int(inputhere[0]) == 1:
        myqueue.appendleft(int(inputhere.split(" ")[1]))
    elif int(inputhere[0]) == 2:
        myqueue.pop()
    else:
        print(myqueue[-1])
"""
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2
"""
############################################################
# https://www.springboard.com/workshops/data-engineering-career-track/learn#/curriculum/24186
# Trees
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        """helper function to locate node in level dimension"""
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root
root = build_product_tree()
root.print_tree()


