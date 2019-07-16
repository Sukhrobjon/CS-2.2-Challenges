import sys
from graph import Graph


def read_file(path):
    """Read the txt file containg graph information and return them
    in a list
    """
    with open(path, 'r') as f:
        data = f.read().split('\n')
    return data

def build_graph(filename):
    """Build a graph from given information"""
    
    g = Graph()

    data = read_file(filename)
    # second line in the txt file is the vertices
    vertices_list = data[1].split(',')
    for vertex in vertices_list:
        g.add_vertex(vertex)

    print("# vertices: ", g.get_vertices())
    # Add connections (non weighted edges for now)
    # g.add_edge("Friend 1", "Friend 2")
    # g.add_edge("Friend 2", "Friend 3")

    # # Challenge 1: Output the vertices & edges
    # # Print vertices
    # print("The vertices are: ", g.get_vertices(), "\n")

    # # Print edges
    # print("The edges are: ")
    # for v in g:
    #     for w in v.get_neighbors():
    #         # print("( %s , %s )" % (v.get_id(), w.get_id()))
    #         print(f'({v.get_id()}, {w.get_id()}, {v.get_edge_weight(w)})')

    # print("edges: ", g.get_all_edges())
filename = 'graph_data.txt'
# filename = sys.argv[1]
data = read_file(filename)
# print(data[1].split(','))
print(build_graph(filename),"")


def output_result(graph_data):
    """Print out the Graph in a formated order"""
    pass


# Driver code


if __name__ == "__main__":

    pass




"""
# Vertices: 4
# Edges: 4
Edge List:
(1,2,10)
(1,4,5)
(2,3,5)
(2,4,7)
"""
