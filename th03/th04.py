import heapq

# Danh sách các đỉnh theo thứ tự
vertices = ['a', 'b', 'c', 'f', 'g', 'z']

# a) Biểu diễn ma trận kề (Adjacency Matrix)
INF = float('inf')
adjacency_matrix = [
    # a    b    c    f    g    z
    [  0,   3, INF,   1, INF, INF], # a
    [INF,   0,   7, INF, INF, INF], # b
    [INF, INF,   0, INF, INF,   3], # c
    [INF, INF,   9,   0,   2, INF], # f
    [INF, INF,   3, INF,   0,   7], # g
    [INF, INF, INF, INF, INF,   0]  # z
]

def print_matrix(matrix, vertices):
    print("a) Ma trận kề (Adjacency Matrix):")
    print("      " + "     ".join(vertices))
    for i, row in enumerate(matrix):
        formatted_row = ["∞" if val == INF else str(val) for val in row]
        # Định dạng in cho thẳng cột
        row_str = "  ".join([f"{val:>3}" for val in formatted_row])
        print(f" {vertices[i]}  [{row_str}]")
    print("-" * 40)

# b) tìm đường đi ngắn nhất
def dijkstra(matrix, start_idx, end_idx, vertices):
    n = len(matrix)
    distances = {i: INF for i in range(n)}
    distances[start_idx] = 0
    
    # Lưu vết đường đi
    previous_nodes = {i: None for i in range(n)}
    
    pq = [(0, start_idx)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        if current_node == end_idx:
            break
            
        if current_dist > distances[current_node]:
            continue
            
        # Duyệt qua các đỉnh kề
        for neighbor in range(n):
            weight = matrix[current_node][neighbor]
            if weight != 0 and weight != INF:
                distance = current_dist + weight
                
                # Cập nhật nếu tìm thấy đường đi ngắn hơn
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
                    
    path = []
    current = end_idx
    while current is not None:
        path.append(vertices[current])
        current = previous_nodes[current]
    path.reverse()
    
    return distances[end_idx], path

#Chuong Trinh
if __name__ == "__main__":
    print_matrix(adjacency_matrix, vertices)
    
    start_node = 'a'
    end_node = 'z'
    start_idx = vertices.index(start_node)
    end_idx = vertices.index(end_node)
    
    shortest_distance, shortest_path = dijkstra(adjacency_matrix, start_idx, end_idx, vertices)
    
    print("b) Kết quả tìm đường đi ngắn nhất:")
    print(f" * Đường đi ngắn nhất từ '{start_node}' đến '{end_node}' là: {' -> '.join(shortest_path)}")
    print(f" * Tổng chi phí (độ dài): {shortest_distance}")