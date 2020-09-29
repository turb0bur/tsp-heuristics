import math
import numpy as np
import matplotlib.pyplot as plt


class Graph:

    def __init__(self, points, size=0):
        self.__matrix = np.zeros((size, size))
        self.__size = len(points)
        self.__points = points

        for i, a in enumerate(points):
            for j, b in enumerate(points):
                if self.__matrix[i][j] == 0.0:
                    dist = self.__distance(a, b)
                    self.__matrix[i][j] = dist
                    self.__matrix[j][i] = dist

    def __distance(self, a, b):
        if a == b:
            return 0

        xd = a[0] - b[0]
        yd = a[1] - b[1]
        return math.sqrt(pow(xd, 2) + (pow(yd, 2)))

    def __repr__(self):
        return "<Graph size:%s matrix:%s>" % (self.__size, self.__matrix)

    def __str__(self):
        out = ""

        for line in self.__matrix:
            for i in line:
                out += (str(i) + '\t')
            out += "\n"
        out += "\n"

        return out

    def size(self):
        return self.__size

    def get_distance(self, i, j):
        if i >= self.__size or j >= self.__size:
            return None

        return self.__matrix[i][j]

    def get_matrix(self):
        return self.__matrix.copy()

    def set_distance(self, v, i, j):
        self.__matrix[i][j] = v

    @property
    def points(self):
        return self.__points

    def get_tour_length(self, points=[], edges=[]):
        result = 0
        if points:
            for i in range(self.size()):
                result += self.get_distance(points[i], points[i + 1])
        elif edges:
            for i, j in edges:
                result += self.get_distance(i, j)
        return result

    def plot_tour(self, title: str, plot_size: tuple, tour_points=[], tour_edges=[]):
        if tour_points:
            tour = len(tour_points) - 1
            for i in range(tour):
                x = self.points[tour_points[i]][0]
                y = self.points[tour_points[i]][1]
                dx = self.points[tour_points[i + 1]][0] - self.points[tour_points[i]][0]
                dy = self.points[tour_points[i + 1]][1] - self.points[tour_points[i]][1]
                plt.arrow(x, y, dx, dy, color='g', length_includes_head=True, ls='dashed',
                          head_width=0.2, head_length=0.3)
        elif tour_edges:
            for current, next in tour_edges:
                x = self.points[current][0]
                y = self.points[current][1]
                dx = self.points[next][0] - self.points[current][0]
                dy = self.points[next][1] - self.points[current][1]
                plt.arrow(x, y, dx, dy, color='r', length_includes_head=True, ls='dashed',
                          head_width=0.2, head_length=0.3)

        plt.xlim(0, plot_size[0])
        plt.ylim(0, plot_size[1])
        plt.title(title)
        plt.show()
