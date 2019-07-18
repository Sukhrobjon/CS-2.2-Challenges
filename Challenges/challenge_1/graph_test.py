#!python

from graph import Vertex, Graph
import unittest


class VertexTest(unittest.TestCase):
    def test_init(self):
        vt_1 = Vertex('A')
        assert vt_1.get_id() is 'A'
        assert vt_1.neighbors == {}
        
