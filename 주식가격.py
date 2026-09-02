def solution(prices):
    answer = [0] * len(prices)
        
    stack = []

    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx

        stack.append(i)
        #print(stack)

    # 끝까지 가격이 안 떨어진 것들
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices) - 1 - idx

    return answer


print(solution([1,2,3,2,3]))