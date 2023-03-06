# https://school.programmers.co.kr/learn/courses/30/lessons/77486

from pprint import pprint
import math

def solution(enroll, referral, seller, amount):
    answer = []
    array = dict()
    for name, refer in zip(enroll, referral):
        array[name] = {}
        array[name]["refer"] = refer
        array[name]["get"] = 0
    
    for s_name, count in zip(seller, amount):
        get = count * 100
        person = s_name
        
        while True: # 타고타고 올라가기 위해 while문
            if get < 10:
                array[person]["get"] += get
                break
            
            else:
                array[person]["get"] += math.ceil(get * 0.9)
                person = array[person]["refer"]
                if person == "-":
                    break
                
                get = math.floor(get * 0.1)
            
    return [item["get"] for item in array.values()]

# def solution(enroll, referral, seller, amount):
#     answer = []
#     array = dict()
#     for name, refer in zip(enroll, referral):
#         array[name] = {}
#         array[name]["refer"] = refer
#         array[name]["get"] = 0

#     for s_name, count in zip(seller, amount):
#         array[s_name]["get"] = count * 100
    
#     for n in reversed(enroll):
#         refer_name = array[n]["refer"]
#         if refer_name != "-":
#             array[refer_name]["get"] += math.floor(array[n]["get"] * 0.1)
#             array[n]["get"] = math.ceil(array[n]["get"] * 0.9)
#         else:
#             array[n]["get"] = math.ceil(array[n]["get"] * 0.9)
    
#     return [item["get"] for item in array.values()]

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["sam", "emily", "jaimie", "edward"]
amount = [2, 3, 5, 4]
solution(enroll, referral, seller, amount)