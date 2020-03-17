from util import Stack, Queue
# lets code a bft
"""
    Remember to follow our problem solving framework
    - Understand the problem
    - Plan a solution
    - Implement the solution
"""

# code up a Graph class implementing with an adjacency list

class Graph:
    """ Represent a Graph as dictionary of vertices map the labels to edges."""

    # constructor
    def __init__(self):
        self.vertices = {} # adjacency list (dictionary)
        # self.vertices = [[],[],[]] # adjacency matrix (2d list or array)

    # add vertex
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    # add edges
    def add_edge(self, v1, v2):
        # check that v1 and v2 exist in the vertices dictionary
        if v1 in self.vertices and v2 in self.vertices:
            # add v2 to the vertices at v1
            self.vertices[v1].add(v2)
            # # add v1 to the vertices at v2 bidirectional or undirected
            # self.vertices[v2].add(v1)
        # otherwise
        else:
            # raise and exception and give an error
            raise IndexError("That vertex does not exist")

    # get neighbors
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    # BFT
    def bft(self, starting_vertex_id):
        # create empty queue enqueue the starting vertex id
        q = Queue()
        q.enqueue(starting_vertex_id)
        # create a set to store our visited vertices
        visited = set()

        # while queue is not empty (len greater than 0)
        while q.size() > 0:
            # dequeue the first vertex
            v = q.dequeue()
            # if that vertex has not been visited
            if v not in visited:
                # mark as visited and print for debugging
                visited.add(v)
                print(v) # for debugging
                # iterate over the child vertices of the current vertex
                for next_vertex in self.vertices[v]:
                    # enqueue the next vertex
                    q.enqueue(next_vertex)

    # DFT
    def dft(self, starting_vertex_id):
        # create empty stack push the starting vertex id
        s = Stack()
        s.push(starting_vertex_id)
        # create a set to store our visited vertices
        visited = set()

        # while stack is not empty (len greater than 0)
        while s.size() > 0:
            # pop the first vertex
            v = s.pop()
            # if that vertex has not been visited
            if v not in visited:
                # mark as visited and print for debugging
                visited.add(v)
                print(v) # for debugging
                # iterate over the child vertices of the current vertex
                for next_vertex in self.vertices[v]:
                    # push the next vertex
                    s.push(next_vertex)

    def dft_recursive(self, start_vert, visited=None):
        # if the visited structure is set to None

            # create a new set for visited
            
        
        # add a starting vertex to the visited set
        
        # print the start vertex
        
        # loop over every child vertex in vertices set at the start vertex
        
            # if child vertex is not in visited
            
                # do a recursive call to dft_recursive
                # using the child vertex and the current visited set as arguments
        pass

    def dfs(self, start_vert, target_value, visited=None):
        # if visited is None
        if visited is None:
            # create a new set of visited
            visited = set()
        # add start vert to visited
        visited.add(start_vert)
        # if the start vert is equal to the target value
        if start_vert == target_value:
            # return True
            return True
        # loop over every child vertex in vertices set at the start vertex
        for child_vert in self.vertices[start_vert]:
            # if child vert is not in visited
            if child_vert not in visited:
                # if the recursive call to dfs
                if self.dfs(child_vert, target_value, visited):
                    # return True
                    return True
        # Return False
        return False

    def bfs(self, starting_vertex_id, target_value):
        # create a queue to hold the vertex ids
        q = Queue()
        # enqueue the start vertex id
        q.enqueue(starting_vertex_id)
        # create an empty visited set
        visited = set()
        # while the queue is not empty
        while q.size() > 0:
            # set vert to the dequeued element
            vert = q.dequeue()
            # if the vert is not in visited
            if vert not in visited:
                # if vert is target value
                if vert == target_value:
                    # return True
                    return True
                # add the vert to visited set
                visited.add(vert)
                # loop over next vert in the vertices at the index of vert
                for next_vert in self.vertices[vert]:
                    # enqueue the next vert
                    q.enqueue(next_vert)
        # return False
        return False

    def bfs_path(self, starting_vertex_id, target_value):
        # create a queue
        
        # enqueue a list holding the starting vertex id
        
        # created an empty visited set
        
        # while the queue is not empty
        
            # dequeue to the path
            
            # set a vert to the last item in the path
           
            # if vert is not in visited
            
                # if vert is equal to target value
                
                    # return path
                    
                # add vert to visited set
                
                # loop over next vert in vertices at the index of vert
                
                    # set a new path equal to a new list of the path (copy)
                    
                    # append next vert to new path
                    
                    # enqueue the new path
                    
        # return None
        pass

    def dfs_path(self, starting_vertex_id, target_value):
        pass