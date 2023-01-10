def solution(arr):
    answer = [arr[0]]
    for number in arr[1:]:
        if answer[-1] != number:
            answer.append(number)
    return answer