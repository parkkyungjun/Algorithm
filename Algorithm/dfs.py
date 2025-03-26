def solution(graph, start):
    visitied = set()
    order = []
    
    def dfs(v):
        visitied.add(v)
        order.append(v)
        
        for n in graph.get(v, []):
            if n not in visitied:
                dfs(n)
                
    dfs(start)
    return order
                
                
        
        