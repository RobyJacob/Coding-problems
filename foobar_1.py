def inifinite_sequence():
    num = 2
    while True:
        yield num
        num += 1

def is_prime(num):
    import math
    count = 0
    for n in range(1, int(math.sqrt(num))+1):
        if num % n == 0:
            count += 1
    if count < 2:
        return True
    return False

def solution(i):
    index = 0
    id = ""
    for num in inifinite_sequence():
        if is_prime(num):
            id += str(num)
            index += 1
            if index > i+5:
                break
    return id[i:i+5]


print(solution(3))
print(solution(0))
print(solution(5))
print(solution(10))
print(solution(50))
print(solution(100))
print(solution(300))
print(solution(500))
print(solution(1000))
print(solution(1500))
print(solution(10000))
