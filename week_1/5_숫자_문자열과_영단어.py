# https://school.programmers.co.kr/learn/courses/30/lessons/81301
str_ = 'one4sevenone'
# arr_ = []
# if 'one' in str_:
#     str_arr = str_.split('one')
#     print(str_arr)
#     for i in str_arr:
#         if i == '':
#             print("false")

a = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
}

for i in a:
    if i in str_:
        str_ = str_.replace(i, a[i])
        # print(str_)

if 'one' in str_:
    str_ = str_.replace('one', '1')
    

##############################################

def solution(s):
    answer = 0
    a = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9',
    }

    for i in a:
        if i in s:
            s = s.replace(i, a[i])

    answer = int(s)
    
    return answer
