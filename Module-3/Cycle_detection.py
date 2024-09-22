from collections import deque 
class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

    def hasCycle(self, Graph, start):
        visited=set()
        q=deque()
        parent={}
        q.append(start)
        visited.add(start)
        while q:
            curr=q.popleft()
            for i in curr.neighbors():
                if i not in visited:
                    visited.add(i)
                    q.append(i)
                    parent[i]=curr
                elif parent[i] != curr and i in visited:
                    return True
        return False
    
    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def constructGraph(self):
        for neighbor in self.neighbors:
            neighbor.addNeighbor(self)
      
    


  
    
      


        
            