import sys

# BÀI 1: TẠO DANH SÁCH KỀ (ADJACENCY LIST)
n = 6 # Đồ thị có 6 đỉnh (từ 0 đến 5)
adj = [[] for _ in range(n)]

adj[0] = [(1, 4), (2, 1)]
adj[1] = [(3, 1)]
adj[2] = [(1, 2), (3, 5), (4, 8)]
adj[3] = [(4, 3), (5, 6)]
adj[4] = [(5, 2)]
adj[5] = []

print(f"adj[0] = {adj[0]}")
print(f"adj[2] = {adj[2]}")

import sys

print("-"*50)

# BÀI 2: CHẠY TAY THUẬT TOÁN DIJKSTRA
n = 6
adj = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]

dist = [sys.maxsize] * n
dist[0] = 0
visited = [False] * n
thu_tu_chot = []

for _ in range(n):
    u = -1
    min_dist = sys.maxsize
    for i in range(n):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i
            
    if u == -1: break 
    
    # "Chốt" đỉnh u
    visited[u] = True
    thu_tu_chot.append(u)
    
    for v, weight in adj[u]:
        if not visited[v] and dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight
            
    dist_hien_tai = ['∞' if d == sys.maxsize else d for d in dist]
    print(f"Sau khi chốt đỉnh {u}: dist = {dist_hien_tai}")

print(f"\n=> Thứ tự chốt: {', '.join(map(str, thu_tu_chot))}")

print("-"*50)

# BÀI 3: CÀI ĐẶT HÀM DIJKSTRA TỪ MỘT NGUỒN (O(V^2))
def dijkstra_basic(n, adj, start_node):
    dist = [sys.maxsize] * n
    dist[start_node] = 0
    visited = [False] * n
    
    for _ in range(n):
        u = -1
        min_dist = sys.maxsize
        for i in range(n):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
                
        if u == -1: break
        visited[u] = True
        
        for v, weight in adj[u]:
            if not visited[v] and dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                
    return dist

n = 6
adj = [[(1, 4), (2, 1)], [(3, 1)], [(1, 2), (3, 5), (4, 8)], [(4, 3), (5, 6)], [(5, 2)], []]
s = 0

ket_qua = dijkstra_basic(n, adj, s)
print(f"s = {s} -> dist = {ket_qua}")

print("-"*50)

# BÀI 4: IN KẾT QUẢ KHOẢNG CÁCH CHI TIẾT
dist = [0, 3, 1, 4, 7, 9] 

for i in range(len(dist)):
    # Nếu giá trị vẫn là sys.maxsize (hoặc vô cực) thì in -1
    if dist[i] == sys.maxsize:
        print(f"dist[{i}] = -1")
    else:
        print(f"dist[{i}] = {dist[i]}")

print("-"*50)

# BÀI 5: BẢN RÚT GỌN ĐỒ THỊ VÔ HƯỚNG

# (A=0, B=1, C=2, D=3, E=4)
adj = [
    [(1, 5), (2, 3)],         # A nối với B(5), C(3)
    [(0, 5), (2, 1), (3, 2)], # B nối với A(5), C(1), D(2)
    [(0, 3), (1, 1), (3, 6)], # C nối với A(3), B(1), D(6)
    [(1, 2), (2, 6), (4, 4)], # D nối với B(2), C(6), E(4)
    [(3, 4)]                  # E nối với D(4)
]

n = 5
dist = [float('inf')] * n
dist[0] = 0 # Bắt đầu từ A
visited = [False] * n

# Thuật toán Dijkstra cơ bản
for _ in range(n):
    u = -1
    min_d = float('inf')
    for i in range(n):
        if not visited[i] and dist[i] < min_d:
            min_d = dist[i]
            u = i
            
    visited[u] = True
    
    # Cập nhật khoảng cách các đỉnh kề
    for v, w in adj[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

# In kết quả theo đúng mẫu
ten_dinh = ['A', 'B', 'C', 'D', 'E']
ket_qua = ", ".join([f"{ten_dinh[i]}={dist[i]}" for i in [0, 2, 1, 3, 4]])
print(f"từ A -> {ket_qua}")