

def solution(k, dungeons):
    answer = 0
    
    visited = [False] * len(dungeons)
    
    def dfs(k, count):
        nonlocal answer

        answer = max(answer , count)

        for i in range(len(visited)):
            if visited[i] == False and k >= dungeons[i][0]:
                visited[i] = True
                dfs(k-dungeons[i][1], count + 1)
                visited[i] = False

    dfs(k, 0)
    
    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))