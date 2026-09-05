def solution(people, limit):
    answer = 0

    right = len(people)
    left = 0

    people.sort()

    print(people)

    while left<right:

        right-=1

        if people[right] + people[left] <= limit:
            left+=1

        print(left,right)

        answer+=1

    return answer

print(solution(people=[70,50,80,50],limit = 100))
print(solution(people=[70,80,50],limit = 100))