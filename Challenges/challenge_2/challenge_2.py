import sys
from graph import Graph


def read_file(path):
    """Read the txt file containg graph information and return them
    in a list
    """
    with open(path, 'r') as f:
        data = f.read().split('\n')
    return data

def build_graph(filename, from_vertex, to_vertex):
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
    # add edges
    # for from_vert, to_vert, weight in edges:
    #     g.add_edge(from_vert, to_vert, weight)
        # print("edges: ", from_vert, to_vert, weight)
    for edge in edges:
        g.add_edge(*edge)
        
    

    print("# Vertices: ", len(g.get_vertices()))
    print("# Edges: ", g.get_all_edges())
    print("The Edge List: ")
    for v in g:
        for w in v.get_neighbors():
            print(f'({v.get_id()}, {w.get_id()}, {v.get_edge_weight(w)})')
    shortest_path = g.shortest_path(from_vertex, to_vertex)
    # shortest_path = g.bfs_two(from_vertex, to_vertex)
    print("shortest path:", shortest_path)
    
# with_weight = 'graph_data.txt'
# no_weight = 'graph_no_weight.txt'
filename = sys.argv[1]
# from_vertex = sys.argv[2]
# to_vertex = sys.argv[3]

data = read_file(filename)
build_graph(filename, '1', '5')


if __name__ == "__main__":
    pass
