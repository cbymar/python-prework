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
# import random
# heights = []
# for _ in range(400):
#     tree = binary_search_tree()
#     n_elems = random.choice([100, 1000, 10000, 100000])
#     tree = fill_tree(tree, num_elems=n_elems, max_int=10000000)
#     heights.append((n_elems,tree.height()))
#
#
# import pandas as pd
#
# df = pd.DataFrame(heights, columns=["n_elems","height"])
# df.head()
# df.groupby("n_elems").describe()
# import plotnine as p9
# p = p9.ggplot(data=df, mapping=p9.aes(x="height")) + p9.geom_histogram(binwidth=1) + \
#     p9.facet_wrap("~ n_elems", ncol=1, scales="fixed")
#
# p.save("./ignoreland/aplot.png")
# print(p)

########################################################
# https://www.springboard.com/workshops/data-engineering-career-track/learn#/curriculum/24186
# AVL Tree
# Rebalance via rotate right, rotate left.
# insert.  Start from bottom
class node:
    """used in context of the bst"""
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None  # point to parent node in tree
        self.height = 1


class AVLTree:
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



###########################
# RBTrees
# https://www.springboard.com/workshops/data-engineering-career-track/learn#/curriculum/24186
# Motivation: fewer rotations to balance, and faster insertion/deletion.  AVL is subset of RB.
# RB are not strictly height balanced.
# Left subtree vs right subtree
# height is log2n, and search speed, on average, is O(height). Worst case is O(n)
# Head always black. If node is red, children are black.
# paths to nil nodes must all have same number of black nodes. Path to longest nil node is < 2x shortest.

# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
# def levelOrder(root):
#     #Write your code here
#     outlist = [] # philip charles andrew will harry somekid virginia archie
#     nodeslist = [] # Xphilip Xcharles Xandrew Xwill Xharry Xsomekid Xvirginia Xarchie bud charlotte oscar philipjr ralph sam tim
#     nodeslist.append(root)
#     # while len(nodeslist) > 0:
#     """remove from front of queue and add to outlist"""
#         current = nodeslist.pop(0)
#         outlist.append(current.info)
#         if current.left:
#             nodeslist.append(current.left)  # push onto back of queue
#         if current.right:
#             nodeslist.append(current.right) # push onto back of queue behind left
#     print(outlist)

#                     philip
#     charles                         andrew
#     will    harry              somekid  virginia
# archie bud  charlotte oscar    philipjr ralph sam tim

def levelOrder(root):
    """Use a queue to keep order and an outlist"""
    #Write your code here
    outlist = []
    node_queue = []
    node_queue.append(root)
    while len(node_queue) > 0:
        current = node_queue.pop(0)
        outlist.append(current.info)
        if current.left:
            node_queue.append(current.left)
        if current.right:
            node_queue.append(current.right)
    print(" ".join(map(str,outlist)))

### For reference:
class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

####
# https://www.youtube.com/embed/t0Cq6tVNRBA?autoplay=1&controls=1&showinfo=0&rel=0
# Heaps
# insert at open node, percolate up.
# Remove min node and swap, then percolate down.
# whether node has a parent,
# get the index of left, right, parent
# swap function for two nodes, indexed
# peek method (return, but not remove, min item)
# poll method: unshift and push
# "ensure capacity"??
####
# dict keys can be strings or integers.
# https://www.hackerrank.com/challenges/jesse-and-cookies/problem

import math
import heapq
A = [1, 2, 3, 9, 10, 12]
def cookies(k, A):
    # Write your code here
    heapq.heapify(A)
    flops = 0
    result = -1
    while (len(A) >= 1):
        print(A)
        if (heapq.nsmallest(1, A)[0] >= k):
            result = flops
            break
        flops += 1
        if len(A) > 1:
            heapq.heappush(A, heapq.heappop(A) + 2 * heapq.heappop(A))
        else:
            break
    return result
A = [1, 2, 3, 9, 10, 12]
cookies(13, A)

##############################################
# Trie
# https://www.springboard.com/workshops/data-engineering-career-track/learn#/curriculum/24193
#