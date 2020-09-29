import os
from time import time
from course_work.tsp.graph import Graph
from random import uniform

from course_work.tsp.heuristics import nearest_neighbour_algorithm, nearest_insertion_algorithm


def generate_points(n: int, x_range: int, y_range: int):
    os.chdir("tsp")
    file = 'tsp' + str(n) + '.txt'
    f = open(file, 'w+')
    plot_size = "{} {}\n".format(x_range, y_range)
    f.write(plot_size)
    for i in range(n):
        point = "{:4f} {:4f}\n".format(uniform(x_range / 100, x_range), uniform(y_range / 100, y_range))
        f.write(point)
    f.close()


if __name__ == '__main__':
    # generate_points(500, 800, 800)
    # os.chdir("tsp")
    f = open('tsp100.txt', 'r')
    data = f.read().splitlines()
    f.close()

    plot_x, plot_y = map(int, data[0].strip().split())
    plot_size = (plot_x, plot_y)
    points = []
    for p in range(1, len(data)):
        x, y = map(float, data[p].strip().split())
        points.append((x, y))
    size = len(points)
    graph = Graph(points=points, size=size)

    title = 'Nearest Neighbour Heuristic'
    t0 = time()
    nn_length, nn_tour = nearest_neighbour_algorithm(graph)
    nn_time = time() - t0
    plot_title = "TSP {}\n Number of points: {}\n Tour length: {:.3f}\n Time: {:.4f}".format(title, size, nn_length,
                                                                                             nn_time)
    graph.plot_tour(plot_title, plot_size, tour_points=nn_tour)
    print(title, len(nn_tour) -1, "{:.4f} sec".format(nn_time), sep=' - ')

    title = 'Nearest Insertion Heuristic'
    t0 = time()
    ni_length, ni_tour = nearest_insertion_algorithm(graph)
    ni_time = time() - t0
    plot_title = "TSP {}\n Number of points: {}\n Tour length: {:.3f}\n Time: {:.4f}".format(title, size, ni_length,
                                                                                             ni_time)
    graph.plot_tour(plot_title, plot_size, tour_edges=ni_tour)
    print(title, len(ni_tour), "{:.4f} sec".format(ni_time), sep=' - ')
