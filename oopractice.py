
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

######################
# BST
# https://www.springboard.com/workshops/data-engineering-career-track/learn#/curriculum/24186
# A heap is a....
# BST balance optimizes search; can create self-balancing bsts.
#
class node:
    """used in context of the bst"""
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """The private insert function is recursive"""
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        """Add the left child iff it doesn't exist"""
        if value < cur_node.value:
            if cur_node.left_child==None:
                cur_node.left_child = node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child==None:
                cur_node.right_child = node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("value already in tree")

    def print_tree(self):
        """Two functions: one recursive, one not"""
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node != None:
            self._print_tree(cur_node.left_child)
            print(str(cur_node.value))
            self._print_tree(cur_node.right_child)

    def height(self):
        """This is the public function; calls private function"""
        if self.root != None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        """This is the recursive private function"""
        if cur_node == None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height + 1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root != None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value==cur_node.value:
            return True
        elif value<cur_node.value and cur_node.left_child != None:
            return self._search(value, cur_node.left_child)
        elif value>cur_node.value and cur_node.right_child != None:
            return self._search(value, cur_node.right_child)


def fill_tree(tree, num_elems=100, max_int=1000):
    """Add arbitrary values to the tree"""
    from random import randint
    for _ in range(num_elems):
        cur_elem = randint(0, max_int)  # something from 1:1000
        tree.insert(cur_elem)
    return tree

tree = binary_search_tree()
tree = fill_tree(tree)

tree.print_tree()
print("tree height: " + str(tree.height()))

tree = binary_search_tree(); tree = fill_tree(tree); print(tree.height())
import random
heights = []
for _ in range(400):
    tree = binary_search_tree()
    n_elems = random.choice([100, 1000, 10000, 100000])
    tree = fill_tree(tree, num_elems=n_elems, max_int=10000000)
    heights.append((n_elems,tree.height()))


import pandas as pd

df = pd.DataFrame(heights, columns=["n_elems","height"])
df.head()
df.groupby("n_elems").describe()
# import plotnine as p9
# p = p9.ggplot(data=df, mapping=p9.aes(x="height")) + p9.geom_histogram(binwidth=1) + \
#     p9.facet_wrap("~ n_elems", ncol=1, scales="fixed")
#
# p.save("./ignoreland/aplot.png")
# print(p)


