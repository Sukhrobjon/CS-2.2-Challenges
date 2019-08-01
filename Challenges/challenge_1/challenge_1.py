# import sys
# from graph import Graph


# def read_file(path):
#     """Read the txt file containg graph information and return them
#     in a list
#     """
#     with open(path, 'r') as f:
#         data = f.read().split('\n')
#     return data

# def build_graph(filename):
#     """Build a graph from given information"""
    
#     g = Graph()

#     data = read_file(filename)
#     # second line in the txt file is the vertices
#     vertices_list = data[1].split(',')
#     # add vertices
#     for vertex in vertices_list:
#         g.add_vertex(vertex)

#     # from third line in the data file all are the edges
#     edges = []
#     for edge in data[2:]:
#         # remove the parentheses and split by comma
#         # think about how to add 0 if weight not given
#         edge = tuple(edge.strip("()").split(','))
#         edges.append(edge)
   
#     for edge in edges:
#         g.add_edge(*edge)
        
    
#     print("# Vertices: ", len(g.get_vertices()))
#     print("# Edges: ", g.num_edges)
#     print("The Edge List: ")
#     for edge in g.get_edges():
#         print(edge)

    
# # with_weight = 'graph_data.txt'
# # no_weight = 'graph_no_weight.txt'
# filename = sys.argv[1]
# data = read_file(filename)
# build_graph(filename)


# if __name__ == "__main__":
#     pass


import sys
from graph import Graph, build_graph
from read_file import read_file


def main(filename):

    graph, vertices, edges = read_file(filename)
    graph = build_graph(graph, vertices, edges)

    seperator = "==============================="

    from_vertex = "1"
    to_vertex = "5"

    # grab the edges and vertices from graph object
    g_edges = graph.edge_list
    g_vertices = graph.get_vertices()

    # print(f'{seperator}Start{seperator}')

    # print(f'Vertices: {g_vertices}')
    # print(f'Number of Edges: {len(g_edges)}')
    # print("The Edge List:")
    # for edge in g_edges:
    #     print(edge)

    # print(f'{seperator}BFS order{seperator}')
    # bfs_order = graph.breadth_first_search_traversal(from_vertex)
    # print(bfs_order[0])

    # print(f'{seperator}Shortest Path{seperator}')
    # shortest_path = graph.find_shortest_path(from_vertex, to_vertex)
    # print(f"Verticies in shortest path: {shortest_path[0]}")
    # print(f"Number of edges in shortest path: {shortest_path[1]}")

    # print(f'{seperator}N level connections{seperator}')
    # print(graph.n_level_bfs(from_vertex, 1))

    print(f'{seperator}DFS order traversal{seperator}')
    print((graph.dfs_recursive(from_vertex)))

    print(f'{seperator}DFS find path{seperator}')
    path = (graph.dfs_paths(from_vertex, to_vertex, set()))
    print(f"{bool(path)}")
    print(path[::-1])


if __name__ == "__main__":
    # filename = sys.argv[1]
    filename = 'graph_no_weight.txt'
    main(filename)

