import collections
from collections import deque

class btnode:
    # use exec(open('binaryTree.py').read()) to load these structures in shell
    def __init__(self, val, freq=1):  # constructor, default value
        self.left = None
        self.right = None
        self.val = val
        self.threaded = False
        self.parent = None
        self.freq = freq

##  function to add the elements in the tree
    def add(self, data):
        if (data < self.val) :
            if (self.left):
                self.left.add(data)
            else:
                self.left = btnode(data)
                self.left.parent = self
        else:
            if (self.right):
                self.right.add(data)
            else:
                self.right= btnode(data)
                self.right.parent = self
##
    def inorder_print(self):
        if ( self.left): 
            self.left.inorder_print()
        print(self.val),
        if ( self.right):
            self.right.inorder_print()
##
    def non_recursive_inorder(self):
        q = deque()
        node = self
        q.append(node)
        while(q):
            if (node.left):
                node = node.left
                q.append(node)
            else :
                loop = 1
                while (q and loop) :
                    node = q.pop()
                    if node :
                        print node.val , 

                    if (node.right):
                        node = node.right
                        q.append(node)
                        loop = 0

## find a node
    def find_node(self, val):
        if (val == self.val):
            return self
        elif (val < self.val) :
            if ( self.left):
                return self.left.find_node(val)
            else:
                return "not found"
        else :
            if (self.right):
                return self.right.find_node(val)
            else:
                return "Not found"

    def bt_find_min(self):
        node = self
        while node and node.left :
            node = node.left
        else:
            return node

## find successor of a node
##  if :
        #Right Tree is present, find the min in the right tree
##  else 
        #Find the lowest Ancestor which has this node in its left 
        #subtree
    def find_successor(self):
        node = self
        if (node and node.right) :
            return node.right.bt_find_min()
        else:
            while ( node.parent and (node.parent.right == node)):
                node = node.parent
            return node.parent

    def inorder_3(self):
        node = self.bt_find_min()
        while node:
            print node.val
            node = node.find_successor()


class btree:
    def __init__(self, keys=[15, 6, 18, 3, 2, 7, 13, 9, 17, 20]):
        self.root = None
        self.create_tree(keys)

## Function to create the default tree for practice problems
    def create_tree(self, vals):
        for i in vals:
            self.add(i)

##  add elements to the tree
    def add(self, data):
        if (self.root == None):
            self.root = btnode(data)
        else: 
            self.root.add(data)

    def tprint(self):
        if(self.root != None):
            print "recursive"
            self.root.inorder_print()
            print
            print "Non recursive"
            self.root.non_recursive_inorder()
        else:
            print ("empty tree")

## delete a node from the tree with key
    def delete(self, key):
        if (self.root):
            tnode = self.find_node(key)
            if (tnode.left != None and tnode.right != None):
                print "handle succesor case"
                suc = tnode.find_successor()
                tmp = suc.val
                self.delete(tmp)
                tnode.val = tmp
                return
            elif (tnode.left):
                nchild = tnode.left 
            elif (tnode.right):
                nchild = tnode.right
            else : 
                nchild = None

            if (tnode == tnode.parent.left):
                tnode.parent.left = nchild
            else:
                tnode.parent.right = nchild

            if (nchild) :
                nchild.parent = tnode.parent
                if (nchild.parent == None):
                    self.root = nchild
        return

## function to find a node in the tree
    def find_node(self, val):
        if (self.root):
            return self.root.find_node(val)

## in the default tree find successor of 15, 20, 6, 2, 4
    def find_successor(self, num):
        node = self.find_node(num)
        suc = node.find_successor()
        if suc :
            return suc.val
        else:
            print "Successor Not found"


##  The main program

class optimal_bst(btree):   ## class inheritance: atg
    #   The tree maints three structures to store the information
    #   w[i][j] respresents the sum of frequencies for nodes from i to j
    #   root[i][j] represents the root of a tree for nodes from i to j
    #   cost [i][j] represets the cost of lookup in a tree for nodes i->j

    def __init__ (self, keys=[12, 15, 20,25], freq=[4,3,6,2]):
        self.root = None
        self.keys = keys
        self.freq = freq
        tmp = len(keys)
        self.w = [[0] * tmp for i in range(tmp)]
        self.cost = [[0] * tmp for i in range(tmp)]
        self.root_index = [[0] * tmp for i in range(tmp)]
        ## initialise the cost, w and root index for a tree with single node
        for i in range(tmp): 
            self.w[i][i] = self.freq[i] ## 
            self.cost[i][i] = freq[i]
            self.root_index[i][i] = i
        #self.create_optimal_bst()

#   the function to determine the minimum cost of tree from i to j 
#   and the root index of the tree
#   the cost of tree rooted at k between i,j is 
#   cost[i][k-1] + cost [k+1][j] + w[i][j]. 
#   Special cases to handle when k = i and k = j
    def min_cost(self, i , j):
        self.root_index[i][j] = i
        cur_cost = 0
        min_cost = 0xFFFF;
        for k in range(i, j+1):
            if (k == i):
                cur_cost = self.cost[i+1][j]
            elif (k == j): 
                cur_cost = self.cost[i][k-1]
            else :
                cur_cost = self.cost[i][k-1]
                cur_cost = cur_cost + self.cost[k+1][j]

#   if the cost at index k is min so far store cost and k
            if (cur_cost < min_cost):
                self.root_index[i][j] = k
                min_cost = cur_cost

#print i, k, min_cost, min_cost + self.w[i][j]
        return (min_cost + self.w[i][j]) 

##  Function to create the OBST. 
##  in an obst, each subtree will be obst too. 
##  So yu have to determine the min cost for each such sub obst. 
##  you can keep the results in a table to run the algo in polynomial order
##  For a single node tree the cost is same as frequency and has  already 
##  been initialised. so start from 2 nodes ( n=1)
    def create_optimal_bst(self):
        max_nodes = len(self.freq)
        for n in range(1, max_nodes):  
            ## for each sub obst with a given number of nodes
            for i in range(max_nodes-n): 
                j = n+i
                self.w[i][j] = self.w[i][j-1] + self.w[i+1][j]-self.w[i+1][j-1] 
                cost = self.min_cost(i,j)
                self.cost[i][j] = cost


if __name__ == '__main__' :
    t = btree()
