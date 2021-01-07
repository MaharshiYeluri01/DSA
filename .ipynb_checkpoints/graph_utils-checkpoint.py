import random
import pdb 
from IPython.display import Image
from collections import deque

class Edge:
    def __init__(self,key):
        self.key=key
        self.connectedTo={}
        self.state=0
        
    def addEdge(self,key,w=0):
        self.connectedTo[key]=0
        
    def getConnections(self):
        return self.connectedTo.keys()
        
class Graph:
    def __init__(self):
        self.n_nodes=0
        self.nodes={}
        
    def createNode(self,node):
        self.n_nodes+=1
        self.nodes[node]=Edge(node)
        return self.nodes[node]
    
    def creteConnection(self,v1,v2):
        if v1 not in self.nodes:
            self.createNode(v1)
        if v2 not in self.nodes:
            self.createNode(v2)
        self.nodes[v1].addEdge(v2)
        
    def getNode(self,key):
        if key in self.nodes:
            return self.nodes[key]
        return None
    def __iter__(self):
        return iter(self.nodes.values())
        
def create_graph(edges,directed=False):
    g=Graph()
    for v1,v2 in edges:
        g.creteConnection(v1,v2)
        if not directed:g.creteConnection(v2,v1)
    return g

graphData=edges=[('a','b'),('a','c'),('a','e'),('a','d'),
('b','e'),
('c','g'),('c','d'),('c','e'),
('d','f'),
('e','f'),
('f','g')]