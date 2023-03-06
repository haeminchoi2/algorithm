# https://school.programmers.co.kr/learn/courses/30/lessons/77485
from pprint import pprint
def solution(rows, columns, queries):
    answer = []

    # 처음 배열 만들기
    array = [[0 for _ in range(columns)] for _ in range(rows)]
    number = 1
    for i in range(rows):
        for j in range(columns):
            array[i][j] = number
            number += 1
    
    
    for query in queries: # 쿼리대로 꼭지점과 숫자들 채워넣기
        points = []
        numbers = []
        x1, y1, x2, y2 = query
        for row in range(x1 - 1, x2):
            for col in range(y1 - 1, y2): # right
                points.append([row, col])
                
                if col == y2 - 1:
                    for a in range(x1, x2): # down
                        points.append([a, col])
                        
                        if a == x2 - 1:
                            for b in range(y2 - 2, y1 - 2, -1): # left
                                points.append([a, b])
                                
                                if b == y1 - 1:
                                    for c in range(x2 - 2, x1 - 1, -1): # up
                                        points.append([c, b])
            break

        for point_x, point_y in points: # 최소값 구하기
            numbers.append(array[point_x][point_y])
        answer.append(min(numbers))
        
        for index, number in enumerate(numbers): # 숫자 옮기기
            if index == len(numbers) - 1:
                to_x, to_y = points[0]
                array[to_x][to_y] = number
            else:
                to_x, to_y = points[index + 1]
                array[to_x][to_y] = number
    
    print(answer)
    return answer

solution(100, 97, [[1,1,100,97]])