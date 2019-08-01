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

    print(f'{seperator} Challenge 2 {seperator}')
    
    path, path_len = graph.find_shortest_path(from_vertex, to_vertex)
    
    if path:
        print("Verticies in shortest path: ", end="")
        for i, vert in enumerate(path):
            if i < len(path)-1:
                print(vert, end=", ")
            else:
                print(vert)
        print(f"Number of edges in shortest path: {path_len}")


if __name__ == "__main__":
    main()


#
