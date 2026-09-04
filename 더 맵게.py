import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K and len(scoville) >= 2:
        #print(scoville)
        answer+=1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        heapq.heappush(scoville, first+second*2)
    
    return answer if scoville[0] >= K else -1


print(solution([1, 2, 3, 9, 10, 12], 7))