import sys
import heapq

# TẠO ĐỒ THỊ G1 DÙNG CHUNG (Bài 11 -> 14)

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
# BÀI 11: NHIỀU NGUỒN (MULTI-SOURCE)
# ==========================================
print("=== BÀI 11 ===")
nguon = [0, 3] # Tập đỉnh nguồn
dist_11 = [sys.maxsize] * n_G1
pq_11 = []

for s in nguon:
    dist_11[s] = 0
    heapq.heappush(pq_11, (0, s))

while pq_11:
    d, u = heapq.heappop(pq_11)
    if d > dist_11[u]: 
        continue
    for v, w in adj_G1[u]:
        if dist_11[u] + w < dist_11[v]:
            dist_11[v] = dist_11[u] + w
            heapq.heappush(pq_11, (dist_11[v], v))

print(f"Nguồn = {nguon} -> dist = {dist_11}")
print("-" * 50)


# ==========================================
# BÀI 12: ĐI QUA ĐỈNH BẮT BUỘC
# ==========================================
print("=== BÀI 12 ===")
def get_dijkstra_dist(start, n, adj):
    dist = [sys.maxsize] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

s_12, k_12, t_12 = 0, 2, 5
# Chi phí = (s -> k) + (k -> t)
dist_from_s = get_dijkstra_dist(s_12, n_G1, adj_G1)
dist_from_k = get_dijkstra_dist(k_12, n_G1, adj_G1)

tong_chi_phi = dist_from_s[k_12] + dist_from_k[t_12]
print(f"s={s_12}, t={t_12}, qua k={k_12} -> Tổng độ dài: {tong_chi_phi}")
print("-" * 50)


# ==========================================
# BÀI 13: ĐẾM SỐ ĐƯỜNG ĐI NGẮN NHẤT
# ==========================================
print("=== BÀI 13 ===")
s_13 = 0
dist_13 = [sys.maxsize] * n_G1
count_13 = [0] * n_G1 

dist_13[s_13] = 0
count_13[s_13] = 1
pq_13 = [(0, s_13)]

while pq_13:
    d, u = heapq.heappop(pq_13)
    if d > dist_13[u]: continue
    
    for v, w in adj_G1[u]:
        new_d = d + w
        # Nếu tìm thấy đường NGẮN HƠN, cập nhật lại khoảng cách và thừa kế số cách đi từ u
        if new_d < dist_13[v]:
            dist_13[v] = new_d
            count_13[v] = count_13[u]
            heapq.heappush(pq_13, (dist_13[v], v))
        # Nếu tìm thấy đường BẰNG khoảng cách ngắn nhất, cộng dồn số cách đi
        elif new_d == dist_13[v]:
            count_13[v] += count_13[u]

for i in range(n_G1):
    print(f"Đỉnh {i}: Độ dài ngắn nhất = {dist_13[i]}, Số lượng đường đi = {count_13[i]}")
print("-" * 50)


# ==========================================
# BÀI 14: ĐƯỜNG ĐI NGẮN NHÌ (SECOND SHORTEST PATH)
# ==========================================
print("=== BÀI 14 ===")
s_14, t_14 = 0, 4
dist1 = [sys.maxsize] * n_G1 # Lưu đường đi ngắn nhất
dist2 = [sys.maxsize] * n_G1 # Lưu đường đi ngắn nhì

dist1[s_14] = 0
pq_14 = [(0, s_14)]

while pq_14:
    d, u = heapq.heappop(pq_14)
    if d > dist2[u]: continue # Lớn hơn cả ngắn nhì thì bỏ qua
    
    for v, w in adj_G1[u]:
        new_d = d + w
        # Nếu tìm thấy khoảng cách mới nhỏ hơn ngắn nhất hiện tại
        if new_d < dist1[v]:
            dist2[v] = dist1[v] # Đẩy ngắn nhất cũ xuống thành ngắn nhì
            dist1[v] = new_d    # Cập nhật ngắn nhất mới
            heapq.heappush(pq_14, (dist1[v], v))
            heapq.heappush(pq_14, (dist2[v], v))
        # Nếu lớn hơn ngắn nhất nhưng nhỏ hơn ngắn nhì
        elif dist1[v] < new_d < dist2[v]:
            dist2[v] = new_d
            heapq.heappush(pq_14, (dist2[v], v))

print(f"Từ {s_14} tới {t_14}: Ngắn nhất = {dist1[t_14]}, Ngắn nhì = {dist2[t_14]}")
print("-" * 50)


# ==========================================
# BÀI 15: DIJKSTRA TRÊN LƯỚI (GRID)
# ==========================================
print("=== BÀI 15 ===")
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

R, C = len(grid), len(grid[0])
dist_15 = [[sys.maxsize] * C for _ in range(R)]

# Bắt đầu từ ô trên trái (0, 0)
dist_15[0][0] = grid[0][0]
pq_15 = [(grid[0][0], 0, 0)]

# 4 Hướng di chuyển: Xuống, Lên, Phải, Trái
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while pq_15:
    d, r, c = heapq.heappop(pq_15)
    
    if r == R - 1 and c == C - 1:
        break
        
    if d > dist_15[r][c]: 
        continue
        
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        # Kiểm tra xem có đi ra ngoài bản đồ không
        if 0 <= nr < R and 0 <= nc < C:
            new_cost = d + grid[nr][nc]
            if new_cost < dist_15[nr][nc]:
                dist_15[nr][nc] = new_cost
                heapq.heappush(pq_15, (new_cost, nr, nc))

print(f"Lưới 3x3 -> Tổng chi phí nhỏ nhất tới đích là: {dist_15[R-1][C-1]}")
