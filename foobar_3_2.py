# find divisors of l[index] by looking at values below l[index]
def divisors(l, index):
    return len([num for num in l[:index] if l[index] % num == 0])

# find multiples of l[index] by looking at values above l[index]
def multiples(l, index):
    return len([num for num in l[index+1:] if num % l[index] == 0])

def solution(l):
    # keep track of the count of the product of multiples and divisors
    count = 0

    # for each number in the list find its multiples and divisors then take its product
    # and finally count up all the products
    for i in range(len(l)):
        count += multiples(l, i) * divisors(l, i)

    return count

print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1, 1, 1]))
print(solution([1, 3, 5]))
print(solution(range(1, 2001)))
