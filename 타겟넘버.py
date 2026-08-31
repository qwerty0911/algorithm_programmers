answer=0
def solution(numbers, target):
    global answer
    
    dfs(0,0,target,numbers)
    
    return answer


def dfs(index, total, target, numbers):
    global answer
    
    if index == len(numbers):
        if target == total:
            answer +=1
            
    else:
        dfs(index+1, total + numbers[index], target, numbers)
        dfs(index+1, total - numbers[index], target, numbers)

#print(solution([1,1,1,1,1],3))
print(solution([4,1,2,1],4))