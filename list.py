class list_node:
    def __init__(self, data=None, nextn=None):
        self.nextn = nextn 
        self.val = data

    def __str__(self):
        return str(self.val)

class list:
    def __init__(self):
        self.head = None 
        self.tail = None
        self.size = 0

    def __str__(self):
        if (self.head == None):
            return "Empty List"
        else:
            out = " "
            tmp_node=self.head
            while(tmp_node):
                out = out+ " "+ str(tmp_node)
                tmp_node = tmp_node.nextn
        return out

##  Insert a given node in the linked list
##  Node this function takes the node to be inserted whereas
##  delete() function takes the value corresponding to node to be dleted
    def insert_node(self, node):
        if (self.head == None):
            self.head = node
        else:
            tmp_node = self.get_last()
            tmp_node.nextn = node
        self.size = self.size+1

    def insert(self, val):
        node = list_node(val)
        if (self.head == None):
            self.head = node
        else:
            tmp_node = self.get_last()
            tmp_node.nextn = node
        self.size = self.size+1

    def get_last(self):
        if (self.head == None):
            return self.head
        else:
            tmp_node = self.head
            while (tmp_node):
                if tmp_node.nextn == None:
                    return tmp_node
                else :
                    tmp_node = tmp_node.nextn

##  Delete a node from the list
##  Node to be deleted is determined from the given val
    def delete(self, val):
        if (self.head == None):
            return
        else:
##  Head node delete case##############
            self.size = self.size-1
            if (self.head.val == val):
                self.head = self.head.nextn
                return

            tmp_node = self.head
            prev_node =tmp_node
            while(tmp_node):
                if tmp_node.val == val:
                    prev_node.nextn = tmp_node.nextn 
                    break;
                prev_node =tmp_node
                tmp_node = tmp_node.nextn

    def find(self, val):
        if (self.head == None):
            return None
        else:
            tmp_node = self.head
            while(tmp_node): 
                if (val == tmp_node.val):
                   return tmp_node
                tmp_node = tmp_node.nextn

    def list_size(self):
        return self.size

if __name__ == '__main__':
    a = list()
    a.insert(10)
    a.insert(20)
    a.insert(30)
    pass
