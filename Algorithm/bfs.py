from collection import deque

def solution(graph, start):
    visited = set([start])
    q = deque([start])
    order = []
    
    while q:
        now = q.pop()
        order.append(now)
        
        for n in graph.get(now, []):
            if n not in visited:
                q.append(now)
                visited.add(now)
    
    return order
        