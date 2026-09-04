import collections

def solution(priorities, location):
    answer = 0
    
    q = collections.deque()
    
    for i in range(len(priorities)):
        q.append([priorities[i],i])
        
    while True:
        current = q.popleft()
        if current[0] < max(item[0] for item in q):
            q.append(current)
            
        else:
            answer+=1

            if current[1] == location:
                return answer

print(solution([2,1,3,2],4))