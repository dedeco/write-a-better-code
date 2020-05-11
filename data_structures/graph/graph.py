
from .vertex import Vertex


class Graph:

    def __init__(self, directed=False):
        self.vertex = {}
        self.directed = directed

    def insert_vertex(self, id):
        v = Vertex(id)
        self.vertex[id] = v
        return v

    def insert_edge(self, _from, _to, distance):
        if _from not in self.vertex:
            self.insert_vertex(_from)
        if _to not in self.vertex:
            self.insert_vertex(_to)
        if distance:
            self.vertex[_from].insert_vertex_adjacent(self.vertex[_to], distance)
            if not self.directed:
                self.vertex[_to].insert_vertex_adjacent(
                    self.vertex[_from], distance)

    def get_vertex(self, id):
        if id in self.vertex:
            return self.vertex[id]
        else:
            return None

    def get_vertexs(self):
        return [v for k,v in self.vertex.items()]
