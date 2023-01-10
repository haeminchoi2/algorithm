def solution(a, b):
    if a == b:
        return a
    
    if a > b:
        numbers = range(b, a+1)
        return sum(numbers)
    
    else:
        numbers = list(range(a, b+1))
        return sum(numbers)
    
solution(3, 5)