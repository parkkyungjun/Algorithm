# target과 동일한 값이 있을때
def solution(arr, target):
    arr = sorted(arr)
    left, right = 0, len(arr)-1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1 
    return

# target과 가장 가까운 값 찾기
def solution(arr, target):
    arr = sorted(arr)
    left, right = 0, len(arr)-1
    
    best = arr[0]
    while left <= right:
        mid = (left + right) // 2
        
        if abs(arr[mid] - target) < abs(best - target):
            best = arr[mid]
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return best
            
# target과 가장 가까운면서 가장 작은 인덱스 찾기
def solution(arr, target):
    arr = sorted([[index, i] for index, i in enumerate(arr)], key=lambda x:x[1])
    left, right = 0, len(arr)-1
    
    best_index, best = arr[0]
    while left <= right:
        mid = (left + right) // 2
        
        index, value = arr[mid]
        if abs(value - target) < abs(best - target):
            best = value
            best_index = index
        elif abs(value - target) == abs(best - target):
            if best_index > index:
                best_index = index
                
        if value > target:
            right = mid - 1
        elif value < target:
            left = mid + 1
        else:
            return best, best_index
            
    return best, best_index