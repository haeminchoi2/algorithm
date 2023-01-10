def solution(absolutes, signs):
    numbers = []
    for index, number in enumerate(absolutes):
        if signs[index] == True:
            numbers.append(number)
        else:
            numbers.append(-number)
    return sum(numbers)