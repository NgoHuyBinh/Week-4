import sys
import heapq

# Tạo mảng cho bài từ 6-10
n_G1 = 6
adj_G1 = [
    [(1, 4), (2, 1)],         # Đỉnh 0
    [(3, 1)],                 # Đỉnh 1
    [(1, 2), (3, 5), (4, 8)], # Đỉnh 2
    [(4, 3), (5, 6)],         # Đỉnh 3
    [(5, 2)],                 # Đỉnh 4
    []                        # Đỉnh 5
]


# ==========================================
# BÀI 6: ĐƯỜNG ĐI NGẮN NHẤT GIỮA HAI ĐỈNH (Dừng sớm)
# ==========================================
print("=== BÀI 6 ===")
s_6, t_6 = 0, 4
dist_6 = [sys.maxsize] * n_G1
dist_6[s_6] = 0
visited_6 = [False] * n_G1

for _ in range(n_G1):
    u = -1
    min_d = sys.maxsize
    for i in range(n_G1):
        if not visited_6[i] and dist_6[i] < min_d:
            min_d = dist_6[i]
            u = i
            
    if u == -1 or u == t_6:
        break
        
    visited_6[u] = True
    for v, w in adj_G1[u]:
        if dist_6[u] + w < dist_6[v]:
            dist_6[v] = dist_6[u] + w

print(f"s = {s_6}, t = {t_6} -> {dist_6[t_6]}")
print("-" * 50)


# ==========================================
# BÀI 7: TRUY VẾT ĐƯỜNG ĐI (Reconstruct path)
# ==========================================
print("=== BÀI 7 ===")
s_7, t_7 = 0, 4
dist_7 = [sys.maxsize] * n_G1
dist_7[s_7] = 0
visited_7 = [False] * n_G1
parent = [-1] * n_G1 

for _ in range(n_G1):
    u = -1
    min_d = sys.maxsize
    for i in range(n_G1):
        if not visited_7[i] and dist_7[i] < min_d:
            min_d = dist_7[i]
            u = i
            
    if u == -1 or u == t_7: 
        break
        
    visited_7[u] = True
    for v, w in adj_G1[u]:
        if dist_7[u] + w < dist_7[v]:
            dist_7[v] = dist_7[u] + w
            parent[v] = u 
path = []
curr = t_7
while curr != -1:
    path.append(curr)
    curr = parent[curr]
    
path.reverse() # Đảo ngược lại để có đường đi đúng từ s tới t
path_str = " -> ".join(map(str, path))
print(f"{path_str} (độ dài {dist_7[t_7]})")
print("-" * 50)


# ==========================================
# BÀI 8: SỐ ĐỈNH TRONG BÁN KÍNH D
# ==========================================
print("=== BÀI 8 ===")
s_8 = 0
D = 3
dist_8 = [sys.maxsize] * n_G1
dist_8[s_8] = 0
visited_8 = [False] * n_G1

for _ in range(n_G1):
    u = -1
    min_d = sys.maxsize
    for i in range(n_G1):
        if not visited_8[i] and dist_8[i] < min_d:
            min_d = dist_8[i]
            u = i
            
    if u == -1: break
    visited_8[u] = True
    for v, w in adj_G1[u]:
        if dist_8[u] + w < dist_8[v]:
            dist_8[v] = dist_8[u] + w

valid_vertices = []
sorted_by_dist = sorted([(dist_8[i], i) for i in range(n_G1)])
for d, i in sorted_by_dist:
    if d <= D:
        valid_vertices.append(i)

print(f"D = {D} -> {len(valid_vertices)} đỉnh ({', '.join(map(str, valid_vertices))})")
print("-" * 50)


# ==========================================
# BÀI 9: DIJKSTRA VỚI HÀNG ĐỢI ƯU TIÊN (Min-Heap)
# ==========================================
print("=== BÀI 9 ===")
def dijkstra_heap(n, adj, start):
    dist = [sys.maxsize] * n
    dist[start] = 0
    
    pq = [(0, start)] 
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue
            
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
                
    return dist

dist_9 = dijkstra_heap(n_G1, adj_G1, 0)
print(f"Kết quả chạy bằng Min-Heap: s = 0 -> dist = {dist_9}")
print("Độ phức tạp O((V+E)log V), cực kì hiệu quả trên đồ thị thưa (nhiều đỉnh, ít cạnh).")
