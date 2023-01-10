def solution(n):
    splited_n = sorted(list(str(n)), reverse=True)
    return int("".join(splited_n))

print(solution(118372))