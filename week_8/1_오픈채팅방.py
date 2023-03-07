# https://school.programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    nicknames = dict()
    for r in record:
        data = r.split()
        if data[0] == "Enter":
            nicknames[data[1]] = data[2]
        elif data[0] == "Change":
            nicknames[data[1]] = data[2]
    
    for i in range(len(record)):
        data = record[i].split()
        if data[0] == "Enter":
            answer.append(f"{nicknames[data[1]]}님이 들어왔습니다.")
        elif data[0] == "Leave":
            answer.append(f"{nicknames[data[1]]}님이 나갔습니다.")

    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])