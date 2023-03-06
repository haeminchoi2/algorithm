# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    dic = dict()
    for phone_num in phone_book:
        dic[phone_num] = 0
    
    for p_num in phone_book:
        is_in = ""
        for num in p_num:
            is_in += num
            if is_in in dic and is_in != p_num:
                return False
    return True