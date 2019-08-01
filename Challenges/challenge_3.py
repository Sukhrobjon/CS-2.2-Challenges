import sys
from graphs.graph import Graph, Vertex, build_graph
from graphs.read_file import read_file


def main():
    filename = sys.argv[1]

    graph, vertices, edges = read_file(filename)
    graph = build_graph(graph, vertices, edges)

    seperator = "==============================="

    # grab the edges and vertices from graph object
    g_edges = graph.edge_list
    g_vertices = graph.get_vertices()

    from_vertex = sys.argv[2]
    to_vertex = sys.argv[3]

    print(f'{seperator} Challenge 3 {seperator}')

    path = graph.dfs_paths(from_vertex, to_vertex)

    
    print(f"There exists a path between vertex {from_vertex} and {to_vertex}: {bool(path)}")
    if path:
        print("Verticies in the path: ", end="")
        for i, vert in enumerate(path[::-1]):
            if i < len(path)-1:
                print(vert, end=",")
            else:
                print(vert)

if __name__ == "__main__":
    main()

