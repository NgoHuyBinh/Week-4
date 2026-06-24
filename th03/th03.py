import sys

class Graph():
    def __init__(cung, dinh):
        cung.m = dinh
        cung.graph = [[0 for column in range(dinh)] 
                      for row in range(dinh)]
        
    def inketqua(cung, L, a, Truoc):
        ten_dinh = ['a', 'b', 'c', 'f', 'g', 'z']
        
        print("Đỉnh nguồn xuất phát từ: ", ten_dinh[a])
        for nut in range(cung.m):
            print("Đỉnh", ten_dinh[a], "đến đỉnh", ten_dinh[nut], "độ dài đường đi là: ", L[nut])
            
        z_index = 5
        path = []
        curr = z_index
        while curr != -1:
            path.append(ten_dinh[curr])
            curr = Truoc[curr]
        path.reverse()
        print("\n=> Đường đi cụ thể từ a đến z là:", " -> ".join(path))

    def duongdinhnhat(cung, L, P):
        min_val = sys.maxsize
        min_index = 0
        for n in range(cung.m):
            if L[n] < min_val and P[n] == False:
                min_val = L[n]
                min_index = n
        return min_index

    def timduongdi(cung, a):
        L = [sys.maxsize] * cung.m
        L[a] = 0
        P = [False] * cung.m
        
        Truoc = [-1] * cung.m 

        for cout in range(cung.m):
            u = cung.duongdinhnhat(L, P)
            P[u] = True
            
            for n in range(cung.m):
                if cung.graph[u][n] > 0 and P[n] == False and L[n] > L[u] + cung.graph[u][n]:
                    L[n] = L[u] + cung.graph[u][n]
                    Truoc[n] = u 

        cung.inketqua(L, a, Truoc)


g = Graph(6)

# Nhập ma trận kề (câu a)
g.graph = [
    [0, 3, 0, 1, 0, 0], # a
    [0, 0, 7, 0, 0, 0], # b
    [0, 0, 0, 0, 0, 3], # c
    [0, 0, 9, 0, 2, 0], # f
    [0, 0, 3, 0, 0, 7], # g
    [0, 0, 0, 0, 0, 0]  # z
]

print("")

g.timduongdi(0)