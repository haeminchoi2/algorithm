# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7, "*"]
    right = [3, 6, 9, "#"]
    mid = [2, 5, 8, 0]
    answer_list = []
    l = "*"
    r = "#"
    for number in numbers:
        if number in left:
            l = number
            answer_list.append("L")
        if number in right:
            r = number
            answer_list.append("R")
        if number in mid:
            l_distance = 0
            r_distance = 0
            if l in left:
                l_distance = abs(left.index(l) - mid.index(number)) + 1
            else:
                l_distance = abs(mid.index(l) - mid.index(number))
            
            if r in right:
                r_distance = abs(right.index(r) - mid.index(number)) + 1
            else:
                r_distance = abs(mid.index(r) - mid.index(number))
        
            if l_distance > r_distance:
                r = number
                answer_list.append("R")
            elif l_distance < r_distance:
                l = number
                answer_list.append("L")
            elif l_distance == r_distance:
                if hand == "right":
                    r = number
                    answer_list.append("R")
                else:
                    l = number
                    answer_list.append("L")
    
    answer = "".join(answer_list)
    
    return answer


# solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")