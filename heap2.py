class hnode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
    def __str__(self):
        return (str(self.key) + ":  "+ str(self.value))

class heap:
    def __init__(self, n = [16,14,10,8,7,9,3,2,4,1]):
        self.n = []
        self.heap_size = 0
        if n:
            self.heap_size = len(n)
            for i in range (len(n)):
                self.n.append(hnode(n[i], None))

    def parent(self, index):
        par = -1
        if (index < self.heap_size):
            if index%2 :
                par = int(index//2)
            else :
                par = int(index//2) - 1 
        if ( par < 0) :
            return None
        return par

    def create_heap(self):
        tmpmax = self.heap_size/2 
        while tmpmax >=0 :
            self.heapify(tmpmax)
            tmpmax -= 1

    def __str__(self):
        for i in self.n:
            print i
        return " " 

class min_heap(heap):
    #def __init__(self, n = [16,14,10,8,7,9,3,2,4,1]):
    def __init__(self, n = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]):
        heap.__init__(self,n)
        self.create_heap()

    def __str__(self):
        for i in self.n:
            print i
        return " " 
    
    def get_min(self):
        if self.heap_size == 0:
            return "empty heap"
        return self.n[0]

    def extract_min(self):
        if self.heap_size == 0:
            print "empty heap"
            return None
        self.heap_size -= 1
        tmp = self.n[0]
        self.n[0] = self.n[self.heap_size]
        self.heapify(0)
        return tmp

    def decrease_key(self, index, val):
        if index >= self.heap_size:
            print "Not valid"
        self.n[index].key = val
        while index and self.n[index].key < self.n[self.parent(index)].key:
            self.n[index], self.n[self.parent(index)] = self.n[self.parent(index)], self.n[index]
            index = self.parent(index)

    def insert(self, key, data = None):
        tn = hnode(key, data)
        self.n.append(tn)
        self.heap_size += 1
        self.decrease_key(self.heap_size-1, key)

#   return true if the node at index i is smaller than its children
    def compare(self, i):
        if i < self.heap_size:
            if (2*i+2) < self.heap_size:
                return self.n[i].key <= self.n[2*i+1].key and self.n[i].key <= self.n[2*i+2].key
            elif (2*i+1) < self.heap_size :
                return self.n[i].key <= self.n[2*i+1].key 
            else :
                return True
        return False

#   heapify maintains the heap property. 
#   goes from top to bottom assuming the heap is good except the 
#   given index
    def heapify(self, index):
        if (self.heap_size <= 0) :
            return
        while (self.compare(index) == False): 
            tmp_index = 2*index + 1
            if (2*index+2 < self.heap_size) :
                if self.n[2*index+1].key > self.n[2*index+2].key :
                    tmp_index = 2*index +2 
            self.n[index], self.n[tmp_index] = self.n[tmp_index], self.n[index]
            index = tmp_index

    def sort(self):
        for i in range(self.heap_size):
            print self.extract_min()

class max_heap(heap):
    #def __init__(self, n = [16,14,10,8,7,9,3,2,4,1]):
    def __init__(self, n = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]):
        heap.__init__(self,n)
        self.create_heap()
   
    def get_max(self):
        if self.heap_size == 0:
            return "empty heap"
        return self.n[0]

    def extract_max(self):
        if self.heap_size == 0:
            return "empty heap"
        self.heap_size -= 1
        tmp = self.n[0]
        self.n[0] = self.n[self.heap_size]
        self.heapify(0)
        return tmp

    def parent(self, index):
        par = -1
        if (index < self.heap_size):
            if index%2 :
                par = int(index//2)
            else :
                par = int(index//2) - 1 
        if ( par < 0) :
            return None
        return par

    def increase_key(self, index, val):
        if index >= self.heap_size:
            print "Not valid"
        self.n[index] = val
        while index and self.n[index] > self.n[self.parent(index)]:
            self.n[index], self.n[self.parent(index)] = self.n[self.parent(index)], self.n[index]
            index = self.parent(index)

    def insert(self, key):
        self.n.append(key)
        self.heap_size += 1
        self.increase_key(self.heap_size-1, key)
        print "hello"

    def compare(self, i):
        if i < self.heap_size:
            if (2*i+2) < self.heap_size:
                return self.n[i] >= self.n[2*i+1] and self.n[i] >= self.n[2*i+2]
            elif (2*i+1) < self.heap_size :
                return self.n[i] >= self.n[2*i+1] 
            else :
                return True
        return False

#   heapify maintains the heap property. 
#   goes from top to bottom assuming the heap is good except the 
#   given index
    def heapify(self, index):
        if (self.heap_size <= 0) :
            return
        while (self.compare(index) == False): 
            tmp_index = 2*index + 1
            if (2*index+2 < self.heap_size) :
                if self.n[2*index+1] < self.n[2*index+2] :
                    tmp_index = 2*index +2 
            self.n[index], self.n[tmp_index] = self.n[tmp_index], self.n[index]
            index = tmp_index

    def decrease_key(self, index, val):
        if index >= self.heap_size :
            return 
        else:
            self.n[index] = val
            self.heapify(index)

   
    def sort(self):
        for i in range(self.heap_size):
            print self.extract_max()


if __name__ == '__main__':
    print "Kool"
