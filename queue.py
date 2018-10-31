from heaps import min_heap
from heaps import max_heap

class min_queue(min_heap):
    def __init__(self,n = [1,3,2,4]):
        min_heap.__init__(self,n)

class max_queue(max_heap):
    def __init__(self,n = [1,3,2,4]):
        max_heap.__init__(self,n)

class lnode:
    def __init__(self, key = None, data = None):
        self.lnext = None
        self.lkey = key
        self.ldata = data

class llist:
    def __init__(self):
        self.lhead = None
        self.lcount = 0

    def insert(self, key, data):
        if (self.lhead == None):
            self.lhead = lnode(key,data)
            self.lcount += 1
        else:
            n = self.lhead
            while n:
                prev = n
                n = n.lnext
            prev.lnext = lnode(key, data)

    def print_list(self):
        n = self.lhead
        while n:
            print n.lkey, n.ldata
            n = n.lnext


if __name__ =='__main__':
    pass
