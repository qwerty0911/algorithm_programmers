import math

def solution(progresses, speeds):
    answer = []
    
    days = [0] * len(progresses)
    
    for i in range(len(progresses)):
        days[i] = math.ceil((100 - progresses[i])/speeds[i])
        
    print(days)
    
    tmp = days[0]
    count = 0
    for day in days:
        if tmp <  day:
            answer.append(count)
            tmp =  day
            count=1
        else:
            count+=1
    
    answer.append(count)
    
    return answer

solution([93,30,55],[1,30,5])