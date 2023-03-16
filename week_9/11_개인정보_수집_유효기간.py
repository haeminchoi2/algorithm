# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    answer = []
    array = {}
    for term in terms:
        name, period = term.split()
        array[name] = int(period)
        
    for index, value in enumerate(privacies):
        date, term = value.split()
        year, month, day = map(int, date.split("."))
        
        month += array[term]
        day -= 1
        while month > 12:
            month -= 12
            year += 1
            
        if day == 0:
            day = 28
            month -= 1
            
        p_date = ".".join([str(year), str(month).zfill(2), str(day).zfill(2)])
        print(p_date)
        if p_date < today:
            answer.append(index+1)
        
    return answer

solution("2021.12.08", ["A 18"], ["2020.06.08 A"])
# "2021.05.02 A", "2021.07.01 B", "2022.02.19 C", 