def solution(arr):
    
    answer = []
    
    for value in arr:
        if not answer or answer[-1] != value:
            answer.append(value)
            tmp = value
    
    return answer

print(solution([1,1,3,3,0,1,1]))