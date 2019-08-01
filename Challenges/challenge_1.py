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

    print(f'{seperator}Start{seperator}')

    print(f'Number of vertices: {len(g_vertices)}')
    print(f'Number of edges: {len(g_edges)}')
    print("The Edge List:")
    for edge in g_edges:
        print(edge)

if __name__ == "__main__":
    main()


# 
