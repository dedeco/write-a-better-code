import sys

from data_structures.graph.graph import Graph


def initialize_single_source(g, s):
    for v in g.get_vertexs():
        v.set_distance(sys.maxsize)
        v.set_visited(False)

    g.get_vertex(s).set_distance(0)


def extract_min(Q):
    min = Q[0]
    for v in Q:
        if v.get_distance() <= min.get_distance():
            min = v
    Q.remove(min)
    return min


def relax(u, v):
    if v.get_distance() > u.get_distance() + u.get_cost(v):
        v.set_distance(u.get_distance() + u.get_cost(v))
        v.set_previous(u)


def dijkstra(g, s):
    initialize_single_source(g, s)

    S = []
    Q = [v for v in g.get_vertexs()]

    while len(Q):

        u = extract_min(Q)

        u.set_visited()

        S.append(u)

        for v in u.get_vertex_adjacents():

            if v.get_visited():
                continue

            relax(u, v)


def find_shortest_path(v, path):
    if v.get_previous():
        path.append(v.get_previous().get_id())
        find_shortest_path(v.get_previous(), path)
    return


def shortestReach(n, edges, s):
    output = []

    g = Graph()

    for i in range(1, n + 1):
        g.insert_vertex(i)

    for x, y, distance in edges:
        g.insert_edge(x, y, distance)

    dijkstra(g, s)

    ordered = sorted([(v.get_id(), v) for v in g.get_vertexs()], key=lambda item: item[0])

    #print([v.get_id() for v in g.get_vertexs()])

    for _, v in ordered:
        if v.get_id() != s:  # exclude source
            path = [v.get_id()]
            find_shortest_path(v, path)
            output.append(-1 if v.get_distance() == sys.maxsize else v.get_distance())
            # print("The shortest paht is {0} with cost {1}".format(path[::-1], v.get_distance()))
    return output


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        edges = []
        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))
        s = int(input())

        result = shortestReach(n, edges, s)
        print(' '.join(map(str, result)))
