#BÀI 16
import heapq

def dijkstra_chi_phi_dinh(so_dinh, danh_sach_canh, chi_phi_dinh, dinh_dau, dinh_cuoi):
    do_thi_mo_rong = {i: [] for i in range(2 * so_dinh)}
    
    for v in range(so_dinh):
        v_vao = v
        v_ra = v + so_dinh
        do_thi_mo_rong[v_vao].append((v_ra, chi_phi_dinh[v]))
        
    for u, v, trong_so_canh in danh_sach_canh:
        u_ra = u + so_dinh
        v_vao = v
        do_thi_mo_rong[u_ra].append((v_vao, trong_so_canh))
        
    dinh_dau_vao = dinh_dau
    dinh_cuoi_ra = dinh_cuoi + so_dinh
    
    khoang_cach = {i: float('inf') for i in range(2 * so_dinh)}
    khoang_cach[dinh_dau_vao] = 0
    
    hang_doi_uu_tien = [(0, dinh_dau_vao)]
    
    while hang_doi_uu_tien:
        chi_phi_hien_tai, u = heapq.heappop(hang_doi_uu_tien)
        
        if chi_phi_hien_tai > khoang_cach[u]:
            continue
            
        if u == dinh_cuoi_ra:
            return khoang_cach[dinh_cuoi_ra]
            
        for dinh_ke, trong_so in do_thi_mo_rong[u]:
            chi_phi_moi = chi_phi_hien_tai + trong_so
            if chi_phi_moi < khoang_cach[dinh_ke]:
                khoang_cach[dinh_ke] = chi_phi_moi
                heapq.heappush(hang_doi_uu_tien, (chi_phi_moi, dinh_ke))
                
    return khoang_cach[dinh_cuoi_ra]


so_luong_dinh = 4
chi_phi_cac_dinh = [2, 5, 1, 3]
cac_canh = [
    (0, 1, 0),
    (0, 2, 0),
    (1, 3, 0),
    (2, 3, 0)
]

bat_dau = 0
ket_thuc = 3

ket_qua = dijkstra_chi_phi_dinh(so_luong_dinh, cac_canh, chi_phi_cac_dinh, bat_dau, ket_thuc)
print("Bài 16: ",ket_qua)

#BAI 17
def dijkstra_bottleneck(do_thi, dinh_dau, dinh_cuoi):
    khoang_cach = {dinh: float('inf') for dinh in do_thi}
    khoang_cach[dinh_dau] = 0
    
    hang_doi_uu_tien = [(0, dinh_dau)]
    
    while hang_doi_uu_tien:
        canh_lon_nhat_hien_tai, u = heapq.heappop(hang_doi_uu_tien)
        
        if canh_lon_nhat_hien_tai > khoang_cach[u]:
            continue
            
        if u == dinh_cuoi:
            return khoang_cach[dinh_cuoi]
            
        for dinh_ke, trong_so in do_thi[u]:
            canh_lon_nhat_moi = max(khoang_cach[u], trong_so)
            
            if canh_lon_nhat_moi < khoang_cach[dinh_ke]:
                khoang_cach[dinh_ke] = canh_lon_nhat_moi
                heapq.heappush(hang_doi_uu_tien, (canh_lon_nhat_moi, dinh_ke))
                
    return khoang_cach[dinh_cuoi]


do_thi_bai_17 = {
    'A': [('B', 3), ('C', 5)],
    'B': [('D', 4), ('C', 1)],
    'C': [('D', 2)],
    'D': []
}

bat_dau = 'A'
ket_thuc = 'D'

ket_qua = dijkstra_bottleneck(do_thi_bai_17, bat_dau, ket_thuc)
print("Bài 17: ",ket_qua)

#BÀI 18
def bellman_ford(so_dinh, danh_sach_canh, dinh_dau):
    khoang_cach = {i: float('inf') for i in range(so_dinh)}
    khoang_cach[dinh_dau] = 0
    
    for _ in range(so_dinh - 1):
        for u, v, trong_so in danh_sach_canh:
            if khoang_cach[u] != float('inf') and khoang_cach[u] + trong_so < khoang_cach[v]:
                khoang_cach[v] = khoang_cach[u] + trong_so
                
    for u, v, trong_so in danh_sach_canh:
        if khoang_cach[u] != float('inf') and khoang_cach[u] + trong_so < khoang_cach[v]:
            return "Do thi co chu trinh am"
            
    return khoang_cach

cac_canh_bai_18 = [
    (0, 1, 2),
    (0, 2, 5),
    (2, 1, -4)
]
print("Bài 18: ",bellman_ford(3, cac_canh_bai_18, 0))

#BAI 19
def dijkstra_xac_suat_lon_nhat(do_thi, dinh_dau, dinh_cuoi):
    xac_suat = {dinh: 0.0 for dinh in do_thi}
    xac_suat[dinh_dau] = 1.0
    
    hang_doi_uu_tien = [(-1.0, dinh_dau)]
    
    while hang_doi_uu_tien:
        xs_hien_tai_am, u = heapq.heappop(hang_doi_uu_tien)
        xs_hien_tai = -xs_hien_tai_am
        
        if xs_hien_tai < xac_suat[u]:
            continue
            
        if u == dinh_cuoi:
            return xac_suat[dinh_cuoi]
            
        for dinh_ke, xs_canh in do_thi[u]:
            xs_moi = xs_hien_tai * xs_canh
            if xs_moi > xac_suat[dinh_ke]:
                xac_suat[dinh_ke] = xs_moi
                heapq.heappush(hang_doi_uu_tien, (-xs_moi, dinh_ke))
                
    return xac_suat[dinh_cuoi]

do_thi_bai_19 = {
    'A': [('B', 0.9), ('C', 0.5)],
    'B': [('D', 0.8)],
    'C': [('D', 0.95)],
    'D': []
}
print("Bài 19: ",dijkstra_xac_suat_lon_nhat(do_thi_bai_19, 'A', 'D'))

#BAI 20
def k_duong_di_ngan_nhat(do_thi, dinh_dau, dinh_cuoi, k):
    dem_so_lan = {dinh: 0 for dinh in do_thi}
    danh_sach_ket_qua = []
    
    hang_doi_uu_tien = [(0, dinh_dau)]
    
    while hang_doi_uu_tien and dem_so_lan[dinh_cuoi] < k:
        khoang_cach_hien_tai, u = heapq.heappop(hang_doi_uu_tien)
        
        if dem_so_lan[u] >= k:
            continue
            
        dem_so_lan[u] += 1
        
        if u == dinh_cuoi:
            danh_sach_ket_qua.append(khoang_cach_hien_tai)
            
        for dinh_ke, trong_so in do_thi[u]:
            if dem_so_lan[dinh_ke] < k:
                heapq.heappush(hang_doi_uu_tien, (khoang_cach_hien_tai + trong_so, dinh_ke))
                
    return danh_sach_ket_qua

do_thi_bai_20 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}
print("Bài 20: ",k_duong_di_ngan_nhat(do_thi_bai_20, 'A', 'D', 3))