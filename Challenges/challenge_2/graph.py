#!python

""" Vertex Class
A helper class for the Graph class that defines vertices and vertex neighbors.
"""

from queue import Queue

class Vertex(object):

    def __init__(self, data):
        """Initialize a vertex and its neighbors.
        neighbors: set of vertices adjacent to self,
        stored in a dictionary with key = vertex,
        value = weight of edge between self and neighbor.
        """
        self.data = data
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """Add a neighbor along a weighted edge."""
        
        if vertex not in self.neighbors.keys():
            self.neighbors[vertex] = weight
        else:
            raise ValueError(f"The vertex: {vertex} already exists!")


    def __str__(self):
        """Output the list of neighbors of this vertex."""
        return f'{self.data} adjacent to {[x.data for x in self.neighbors]}'

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return self.neighbors.keys()

    def get_id(self):
        """Return the id of this vertex."""
        return self.data

    def get_edge_weight(self, vertex):
        """Return the weight of this edge."""
        # vertex to the given vertex.
        return self.neighbors[vertex]
    
    def get_edges(self):
        """Return number of edges of one vertex"""
        return len(self.neighbors.keys())




""" Graph Class
A class demonstrating the essential
facts and functionalities of graphs.
"""

# NOTE: id is the key and vertecies are the values
class Graph:
    def __init__(self):
        """Initialize a graph object with an empty dictionary."""
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.vert_dict.values())

    def add_vertex(self, key):
        """Add a new vertex object to the graph with the given key and return the vertex."""
        # increment the number of vertices
        self.num_vertices += 1
        # create a new vertex
        new_vertex = Vertex(key)
        # add the new vertex to the vertex dictionry
        self.vert_dict[key] = new_vertex
        # return the new vertex
        return new_vertex

    def get_vertex(self, key):
        """Return the vertex if it exists"""
        # return the vertex if it is in the graph
        if key in self.vert_dict.keys():
            return key
        else:
            raise ValueError("No vertex found!")

    def add_edge(self, from_vert, to_vert, weight=0):
        """Add an edge from vertex with key `key1` to vertex with key `key2` with a weight."""
        if from_vert not in self.vert_dict or to_vert not in self.vert_dict:
            # add it - or return an error (choice is up to you).
            raise ValueError("One of the key doesn't exist!")
        else:
            # edge by making key2 a neighbor of key1
            # and using the addNeighbor method of the Vertex class.
            # Hint: the vertex f is stored in self.vert_dict[f].
            self.vert_dict[from_vert].add_neighbor(self.vert_dict[to_vert], weight)
            # self.vert_dict[to_vert].add_neighbor(self.vert_dict[from_vert], weight)

    def get_vertices(self):
        """Return all the vertices in the graph"""
        return self.vert_dict.keys()

    def get_all_edges(self):
        """Return number of all edges in the graph"""
        sum = 0
        for v in self:
            sum += v.get_edges()
        return sum
        
    def shortest_path(self, from_vertex, to_vertex):
        """Search for the shortest path from vertex a to b using Breadth first search
        
        Args:
            from_vertex (str) : starting point on the graph
            to_vertex (str) : the distanation or end of the path

        Returns:
            shortest path (int) : the shortest number of edges between two vertices
        """
        # 
        
        queue = Queue(maxsize=len(self.get_vertices()))
        # enqueue the start vertex
        queue.put(self.vert_dict[from_vertex])
        # keep track of visited vertices with its predessors 
        # the keys are the unique vertices and value is the parent to the associated key 
        # the start node's parent is none
        parent_pointers = {self.vert_dict[from_vertex].data: None}

        while not queue.empty():
            # dequeue 1st vertex in the queue
            current_vertex = queue.get()
            # check if it is the target
            if current_vertex == to_vertex:
                break
            for neighbor in current_vertex.get_neighbors():

                if neighbor not in parent_pointers:
                    new_vertex = self.vert_dict[neighbor]
                    queue.put(new_vertex)
                    
                    # add the new vertex to the parent pointers 
                    parent_pointers[new_vertex] = current_vertex
        
        # Cover case for disjointed graph
        if to_vertex not in parent_pointers:
            return

        path = [self.vert_dict[to_vertex]]

        next_vertex = parent_pointers[to_vertex]

        while next_vertex is not None:
            path.append(next_vertex)
            next_vertex = parent_pointers[next_vertex.data]

        path.reverse()

        return path
# Driver code


if __name__ == "__main__":

    # Challenge 1: Create the graph

    g = Graph()

    # Add your friends
    g.add_vertex("Friend 1")
    g.add_vertex("Friend 2")
    g.add_vertex("Friend 3")

    # ...  add all 10 including you ...

    # Add connections (non weighted edges for now)
    g.add_edge("Friend 1", "Friend 2")
    g.add_edge("Friend 2", "Friend 3")

    # Challenge 1: Output the vertices & edges
    # Print vertices
    print("The vertices are: ", g.get_vertices(), "\n")

    # Print edges
    print("The edges are: ")
    for v in g:
        for w in v.get_neighbors():
            print(f'({v.get_id()}, {w.get_id()}, {v.get_edge_weight(w)})')

    print("edges: ", g.get_all_edges())

