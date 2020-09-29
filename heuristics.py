from random import randrange


def nearest_neighbour_algorithm(graph):
    if graph.size == 0:
        return -1, []

    points = [i for i in range(graph.size())]

    current = randrange(0, graph.size())
    tour = [current]

    points.remove(current)

    while len(points) > 0:
        next = points[0]
        for point in points:
            if graph.get_distance(current, point) < graph.get_distance(current, next):
                next = point
        tour.append(next)
        points.remove(next)
        current = next

    tour.append(tour[0])
    length = graph.get_tour_length(points=tour)

    return length, tour


def nearest_insertion_algorithm(graph):
    if graph.size == 0:
        return -1, []

    points = [i for i in range(graph.size())]

    current = randrange(0, graph.size())
    points.remove(current)

    i = current
    j = points[0]
    cij = graph.get_distance(i, j)
    for point in points:
        if graph.get_distance(i, point) < cij:
            cij = graph.get_distance(i, point)
            j = point

    points.remove(j)

    edges = [(i, j)]

    visited = []
    visited.append(i)
    visited.append(j)

    while len(points) > 0:
        i = visited[0]
        k = points[0]
        crj = graph.get_distance(k, i)

        for point in points:
            for c in visited:
                dist = graph.get_distance(point, c)
                if dist < crj:
                    k = point
        i = edges[0][0]
        j = edges[0][1]
        c_min = graph.get_distance(i, k) + graph.get_distance(k, j) - graph.get_distance(i, j)

        for e in edges:
            aux_i = e[0]
            aux_j = e[1]
            dist = graph.get_distance(aux_i, k) + graph.get_distance(k, aux_j) - graph.get_distance(aux_i, aux_j)
            if dist < c_min:
                c_min = dist
                i = aux_i
                j = aux_j

        if len(edges) == 1:
            edges.append((j, i))
        edges.remove((i, j))
        edges.append((i, k))
        edges.append((k, j))

        visited.append(k)
        points.remove(k)

    length = graph.get_tour_length(edges=edges)

    return length, edges
