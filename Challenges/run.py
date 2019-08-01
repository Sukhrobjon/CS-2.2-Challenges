import sys
from graphs.graph import Graph, Vertex, build_graph
from graphs.read_file import read_file


def main(filename):

    graph, vertices, edges = read_file(filename)
    graph = build_graph(graph, vertices, edges)

    seperator = "==============================="

    from_vertex = "4"
    to_vertex = "1"

    # grab the edges and vertices from graph object
    g_edges = graph.edge_list
    g_vertices = graph.get_vertices()

    print(f'{seperator}DFS order traversal{seperator}')
    print((graph.dfs_recursive(from_vertex)))

    print(f'{seperator}DFS find path{seperator}')
    path = (graph.dfs_paths(from_vertex, to_vertex, set()))
    print(f"{bool(path)}")
    print(path[::-1])


if __name__ == "__main__":
    # filename = sys.argv[1]
    filename = 'inputs/directed_graph.txt'
    main(filename)
