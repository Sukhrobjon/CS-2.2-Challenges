import sys
from graphs.graph import Graph, Vertex, build_graph
from graphs.read_file import read_file


def main():
    filename = sys.argv[1]

    # read from a file to grab graph properties
    graph, vertices, edges = read_file(filename)
    # builded graph object
    graph = build_graph(graph, vertices, edges)

    seperator = "==============================="

    print(f'{seperator}Challenge 5: Eulerian Cycle{seperator}')
    eulerian = graph.is_eulerian()
    print(f"This graph is Eulerian: {eulerian}")

if __name__ == "__main__":
    main()
