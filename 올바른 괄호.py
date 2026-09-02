def solution(s):
    q = []
    tmp = 0
    
    for c in s:
        if c == '(':
            tmp+=1
        else: #c==)
            if tmp == 0:
                return False
            else:
                tmp-=1
                
    if tmp == 0:
        return True
    else:
        return False


print(solution("()()"))