def solution(arr):
    
    answer = []
    
    tmp = 10
    for value in arr:
        if tmp != value:
            answer.append(value)
            tmp = value
    
    return answer

print(solution([1,1,3,3,0,1,1]))