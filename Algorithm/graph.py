def solution(arr):
    n = len(arr)
    graph = {i:[] for i in range(n)}
    
    for i in range(n):
        for j in arr[i]:
            if graph[i][j] != 0:
                graph[i].append(j)
                
    return graph