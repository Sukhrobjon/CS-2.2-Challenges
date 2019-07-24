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
    # add vertices
    for vertex in vertices_list:
        g.add_vertex(vertex)

    # from third line in the data file all are the edges
    edges = []
    for edge in data[2:]:
        # remove the parentheses and split by comma
        # think about how to add 0 if weight not given
        edge = tuple(edge.strip("()").split(','))
        edges.append(edge)
   
    for edge in edges:
        g.add_edge(*edge)
        
    
    print("# Vertices: ", len(g.get_vertices()))
    print("# Edges: ", g.num_edges)
    print("The Edge List: ")
    for edge in g.get_edges():
        print(edge)

    
# with_weight = 'graph_data.txt'
# no_weight = 'graph_no_weight.txt'
filename = sys.argv[1]
data = read_file(filename)
build_graph(filename)


if __name__ == "__main__":
    pass
