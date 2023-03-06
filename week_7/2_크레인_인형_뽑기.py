# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    array = [0] # 초기값 0을 설정, 어차피 0은 빈공간을 의미하므로
    for move in moves:
        for i in range(len(board)):
            if not board[i][move - 1]:
                continue
            else:
                doll = board[i][move - 1]
                
                if array[-1] == doll:
                    array.pop()
                    board[i][move - 1] = 0
                    answer += 2
                    break
                else:
                    array.append(doll)
                    board[i][move - 1] = 0
                    break
    return answer

b = [[0,0,0,0,0],
     [0,0,1,0,3],
     [0,2,5,0,1],
     [4,2,4,4,2],
     [3,5,1,3,1]]
m = [1,5,3,5,1,2,1,4]
print(solution(b, m))