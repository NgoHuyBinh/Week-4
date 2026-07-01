import heapq

#BAI 21
def dijkstra_trang_thai_mo_rong(do_thi, dinh_dau, dinh_cuoi, nhien_lieu_toi_da, chi_phi_nap):
    khoang_cach = {}
    for u in do_thi:
        for f in range(nhien_lieu_toi_da + 1):
            khoang_cach[(u, f)] = float('inf')
            
    khoang_cach[(dinh_dau, nhien_lieu_toi_da)] = 0
    hang_doi_uu_tien = [(0, dinh_dau, nhien_lieu_toi_da)]
    
    while hang_doi_uu_tien:
        chi_phi_hien_tai, u, f_hien_tai = heapq.heappop(hang_doi_uu_tien)
        
        if chi_phi_hien_tai > khoang_cach[(u, f_hien_tai)]:
            continue
            
        if u == dinh_cuoi:
            return chi_phi_hien_tai
            
        if f_hien_tai < nhien_lieu_toi_da:
            if chi_phi_hien_tai + chi_phi_nap[u] < khoang_cach[(u, f_hien_tai + 1)]:
                khoang_cach[(u, f_hien_tai + 1)] = chi_phi_hien_tai + chi_phi_nap[u]
                heapq.heappush(hang_doi_uu_tien, (chi_phi_hien_tai + chi_phi_nap[u], u, f_hien_tai + 1))
                
        for dinh_ke, tieu_hao, trong_so in do_thi[u]:
            if f_hien_tai >= tieu_hao:
                f_moi = f_hien_tai - tieu_hao
                if chi_phi_hien_tai + trong_so < khoang_cach[(dinh_ke, f_moi)]:
                    khoang_cach[(dinh_ke, f_moi)] = chi_phi_hien_tai + trong_so
                    heapq.heappush(hang_doi_uu_tien, (chi_phi_hien_tai + trong_so, dinh_ke, f_moi))
                    
    return float('inf')

do_thi_bai_21 = {
    'A': [('B', 2, 10)],
    'B': [('C', 1, 5)],
    'C': []
}
gia_ve_nap = {'A': 5, 'B': 2, 'C': 10}
print("Bai 21: ",dijkstra_trang_thai_mo_rong(do_thi_bai_21, 'A', 'C', 3, gia_ve_nap))


#BAI 22
def dijkstra_gioi_han_canh(do_thi, dinh_dau, dinh_cuoi, k):
    khoang_cach = {}
    for u in do_thi:
        for c in range(k + 2):
            khoang_cach[(u, c)] = float('inf')
            
    khoang_cach[(dinh_dau, 0)] = 0
    hang_doi_uu_tien = [(0, dinh_dau, 0)]
    
    while hang_doi_uu_tien:
        chi_phi_hien_tai, u, so_canh = heapq.heappop(hang_doi_uu_tien)
        
        if chi_phi_hien_tai > khoang_cach[(u, so_canh)]:
            continue
            
        if u == dinh_cuoi:
            return chi_phi_hien_tai
            
        if so_canh <= k:
            for dinh_ke, trong_so in do_thi[u]:
                if chi_phi_hien_tai + trong_so < khoang_cach[(dinh_ke, so_canh + 1)]:
                    khoang_cach[(dinh_ke, so_canh + 1)] = chi_phi_hien_tai + trong_so
                    heapq.heappush(hang_doi_uu_tien, (chi_phi_hien_tai + trong_so, dinh_ke, so_canh + 1))
                    
    kq = min(khoang_cach[(dinh_cuoi, c)] for c in range(k + 2))
    return kq if kq != float('inf') else -1

do_thi_bai_22 = {
    'A': [('B', 10), ('C', 1)],
    'C': [('B', 1)],
    'B': []
}
print("Bai 22: ",dijkstra_gioi_han_canh(do_thi_bai_22, 'A', 'B', 0))


#BAI 23
def tien_xu_ly_all_pairs(do_thi):
    khoang_cach_toan_bo = {}
    
    for nguon in do_thi:
        khoang_cach = {dinh: float('inf') for dinh in do_thi}
        khoang_cach[nguon] = 0
        hang_doi = [(0, nguon)]
        
        while hang_doi:
            cp, u = heapq.heappop(hang_doi)
            if cp > khoang_cach[u]:
                continue
            for v, ts in do_thi[u]:
                if cp + ts < khoang_cach[v]:
                    khoang_cach[v] = cp + ts
                    heapq.heappush(hang_doi, (khoang_cach[v], v))
                    
        khoang_cach_toan_bo[nguon] = khoang_cach
        
    return khoang_cach_toan_bo

def truy_van_duong_di(khoang_cach_toan_bo, s, t):
    if s in khoang_cach_toan_bo and t in khoang_cach_toan_bo[s]:
        return khoang_cach_toan_bo[s][t]
    return float('inf')

do_thi_bai_23 = {
    'A': [('B', 2)],
    'B': [('C', 3)],
    'C': []
}
du_lieu_goc = tien_xu_ly_all_pairs(do_thi_bai_23)
print("Bai 23: ",truy_van_duong_di(du_lieu_goc, 'A', 'C'))


#BAI 24
def ham_heuristic(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def thuat_toan_a_star(luoi, dinh_dau, dinh_cuoi):
    hang = len(luoi)
    cot = len(luoi[0])
    
    g_score = { (r, c): float('inf') for r in range(hang) for c in range(cot) }
    g_score[dinh_dau] = 0
    
    f_score = { (r, c): float('inf') for r in range(hang) for c in range(cot) }
    f_score[dinh_dau] = ham_heuristic(dinh_dau, dinh_cuoi)
    
    hang_doi_uu_tien = [(f_score[dinh_dau], dinh_dau)]
    so_dinh_da_duyet = 0
    
    while hang_doi_uu_tien:
        _, u = heapq.heappop(hang_doi_uu_tien)
        so_dinh_da_duyet += 1
        
        if u == dinh_cuoi:
            return g_score[dinh_cuoi], so_dinh_da_duyet
            
        r, c = u
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < hang and 0 <= nc < cot and luoi[nr][nc] == 0:
                g_moi = g_score[u] + 1
                if g_moi < g_score[(nr, nc)]:
                    g_score[(nr, nc)] = g_moi
                    f_score[(nr, nc)] = g_moi + ham_heuristic((nr, nc), dinh_cuoi)
                    heapq.heappush(hang_doi_uu_tien, (f_score[(nr, nc)], (nr, nc)))
                    
    return float('inf'), so_dinh_da_duyet

luoi_ban_co = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0]
]
chi_phi, v_duyet = thuat_toan_a_star(luoi_ban_co, (0, 0), (2, 3))
print("Bai 24: ",chi_phi, v_duyet)