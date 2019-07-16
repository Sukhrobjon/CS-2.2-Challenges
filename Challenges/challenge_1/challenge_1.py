import sys


def read_file(txt):
    """Read the txt file containg graph information and return them
    in a list
    """
    with open(txt, 'r') as f:
        data = f.read().split('\n')
    return data[2:]

# filename = 'graph_data.txt'
filename = sys.argv[1]
print(read_file(filename))
def output_result(graph_data):
    """Print out the Graph in a formated order"""
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