import pdb
from queue2 import min_queue
from queue2 import llist

#   A graph representataion as an adjacency list
#   an array of linked lists
#   each element of the array represents a vertex and the list 
#   at that element represents the edges from that vertex.
#   The element of list will basically contain the vertices and edge weights
#   edges is of type { dest_vertex, weight} 
class vertex:
    def __init__(self, key=None, edges = None):
        self.key = key
        self.edges = {} 
        if edges:
            for dest in edges:
                self.edges[dest] = edges[dest]

    def __str__(self):
        return ( str(self.key) + ":  " + str(self.edges)) 
    def add_edge(self, edge):
        for k,v in edge.iteritems():
            self.edges[k] = v

class graph:
    ## gdidct is dictionary of dictionary 
    ## of type {v1: {e1:w1, e2:w2}, v2:{e3:w3,e4:w4}}
    def __init__(self, gdict = None): 
        self.minq = min_queue()
        self.vertices  = {} # vertices and the edges attached to that vertex
        self.mst  = {} 
        self.no = 0
        if gdict:
            for node in gdict:
                self.vertices[node] = vertex(node, gdict[node]) 

    def add_node(self, v1, v2, edge_w):
        if (len(self.vertices) == 0):
            self.vertices[v1] = vertex(v1, {v2:edge_w})
        else: 
            print "before change" , self.vertices
            if v1 in self.vertices.keys():
                self.vertices[v1].add_edge({v2, edge_w})
            if v2 in self.vertices.keys():
                self.vertices[v2].add_edge({v1, edge_w})
            else:
                self.vertices[v1] = vertex(v1, {v2:edge_w})
            print "after change" , self.vertices
            

    def __str__(self):
        for node in self.vertices:
            print self.vertices[node]
        return " graph " 

    def create_min_queue(self, vs):
        i = 0
        for u in vs:
            if u:
                for edge in self.vertices[u]:
                    if edge: 
                        self.minq.insert(self.vertices[u][edge], (u, edge))

    def create_min_wt_queue(self, mq):
        i = 0
        for u in self.vertices:
            if u:
                for edge in self.vertices[u]:
                    if edge: 
                        mq.insert(self.vertices[u][edge], (u, edge))

    def get_number_of_vertices(self):
        for i in self.vertices:
            self.no = self.no + 1
        return self.no

    def get_edge(self, v1, v2):
        if v1 in self.vertices.keys():
            if v2 in self.vertices[v1].keys():
                return v1, v2
        if v2 in self.vertices.keys():
            if v1 in self.vertices[v2].keys():
                return v2, v1

    def prims_mst2(self):
        mq = min_queue()
        maxno = self.get_number_of_vertices() 
        self.create_min_wt_queue(mq)
        m_edge = mq.extract_min()

        while (maxno > 0 and m_edge ):
            maxno = maxno-1
            print "maxno" , maxno
            print m_edge
            print self.vertices[m_edge.value[0]]
            print self.vertices[m_edge.value[1]]

            v1, v2  = self.get_edge(m_edge.value[0], v2 = m_edge.value[1])

            if (len(self.mst) == 0):
                self.mst[v1] = {v2: m_edge.key}
            else: 
                print "before change" , self.mst
                if v1 in self.mst.keys() and v2 in self.mst.keys() :
                    m_edge = mq.extract_min()
                    continue
                elif v1 in self.mst.keys():
                    self.mst[v1][v2] = m_edge.key
                else:
                    self.mst[v1] = {v2: m_edge.key}
            print "after change" , self.mst
            m_edge = mq.extract_min()

    def prims_mst(self):
        mst = graph()   # empty MST graph
        mq = min_queue()
        maxno = self.get_number_of_vertices() - 1
        self.create_min_wt_queue(mq)
        m_edge = mq.extract_min()
        while (maxno > 0 and m_edge ):
            maxno = maxno-1
            print "maxno" , maxno
            print m_edge
            print self.vertices[m_edge.value[0]]
            print self.vertices[m_edge.value[1]]
            if m_edge.value[1] in self.vertices[m_edge.value[0]].keys():
                self.vertices[m_edge.value[0]].pop(m_edge.value[1])
            elif m_edge.value[0] in self.vertices[m_edge.value[1]].keys():
                self.vertices[m_edge.value[1]].pop(m_edge.value[0])

            if m_edge.value[0] in mst.vertices.keys() and m_edge.value[1] in mst.vertices.key() :
                    continue
            elif m_edge.value[0] in mst.vertices.keys():
                self.create_min_queue([m_edge.value[1]])
            elif m_edge.value[1] in mst.vertices.keys():
                self.create_min_queue([m_edge.value[0]])
            else:
                self.create_min_queue([m_edge.value[0], m_edge.value[1]])

            v1 = m_edge.value[0]
            v2 = m_edge.value[1]
            if (len(self.mst) == 0):
                self.mst[v1] = {v2: m_edge.key}
            else: 
                print "before change" , self.mst
                if v1 in self.mst.keys():
                    self.mst[v1][v2] = m_edge.key
                if v2 in self.mst.keys():
                    self.mst[v2][v1] = m_edge.key
                else:
                    self.mst[v1] = {v2: m_edge.key}
            print "after change" , self.mst
         
            print self.mst
            m_edge = self.minq.extract_min()

        return mst 

if __name__ =='__main__':
    exec(open('graph_input.txt').read())
