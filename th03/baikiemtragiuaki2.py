import math
import sys

class Graph:

    def __init__(self, dinh):
        self.x = dinh
        self.graph = [[0 for column in range(dinh)]
                      for row in range(dinh)]

    def inketqua(self, L, a):
        print("Đỉnh nguồn xuất phát từ:", a)

        for nut in range(self.x):
            print(a, "đến đỉnh", nut,
                  "độ dài đường đi là:", L[nut])

    def duongdinhonhat(self, L, P):
        min = sys.maxsize

        for x in range(self.x):
            if L[x] < min and P[x] == False:
                min = L[x]
                min_index = x

        return min_index

    def timduongdi(self, a):
        L = [sys.maxsize] * self.x
        L[a] = 0

        P = [False] * self.x

        for cout in range(self.x):
            u = self.duongdinhonhat(L, P)
            P[u] = True

            for x in range(self.x):
                if (self.graph[u][x] > 0 and
                    P[x] == False and
                    L[x] > L[u] + self.graph[u][x]):

                    L[x] = L[u] + self.graph[u][x]

        self.inketqua(L, a)


# Khởi tạo đồ thị gồm 6 đỉnh
g = Graph(6)

# Ma trận kề
g.graph = [
    [0, 7, 0, 14, 0, 0],
    [0, 0, 4, 1, 0, 0],
    [0, 0, 0, 0, 2, 1],
    [0, 0, 1, 0, 5, 0],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0]
]

# Tìm đường đi ngắn nhất từ đỉnh 0
g.timduongdi(0)