MAX_SIZE = 10

# function to sort(in-place) array of digits using counts
def sort_array_using_counts(arr, n):

    # Store count of all elements
    # Hashmap for number of times each digit appears
    count = [0]*MAX_SIZE
    for i in range(n):
        count[arr[i]] += 1

    # sort the array based on the number of times it occurs first
    # i.e., digit occuring maximum number of times will happen to come first in the array
    index = 0
    for i in range(MAX_SIZE):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1


# Remove elements from arr[] at indexes ind1 and ind2
def print_result(arr, n, ind1, ind2=-1):
    result=[]
    # handling cases for single digit number
    # that is divisible by 3 or not
    if len(arr) == 1:
        if arr[0] % 3 == 0:
            return arr[0]
        else:
            return 0
    # add digits to result
    for i in range(n-1, -1, -1):
        # do not include digits at ind1 and ind2
        if i != ind1 and i != ind2:
            result.append(arr[i])
    # handling case where no digits can be used to form large number divisible by 3
    if len(result) == 0:
        return 0
    # map the digits to string and join them, then convert back to integer
    return int(''.join(map(str, result)))


# Returns largest multiple of 3 that can be formed
# using arr[] elements.
def solution(l):
    if len(l) < 1:
        return 0
    # Sum of all array element
    sum_of_digits = sum(l)

    # Sum is divisible by 3, no need to
    # delete an element
    if sum_of_digits % 3 == 0:
        sort_array_using_counts(l, len(l))
        # print(l)
        return print_result(l, len(l), len(l))

    # Sort array element in increasing order
    sort_array_using_counts(l, len(l))

    # Find reminder
    remainder = sum_of_digits % 3

    # If remainder is '1', we have to delete either
    # one element of remainder '1' or two elements
    # of remainder '2'
    if remainder == 1:
        rem_1 = [0]*2
        rem_1[0] = -1; rem_1[1] = -1

        # Traverse array elements
        for i in range(len(l)):

            # Store first element of remainder '1'
            if l[i] % 3 == 1:
                return print_result(l, len(l), i)

            if l[i] % 3 == 2:

                # If this is first occurrence of remainder 2
                if rem_1[0] == -1:
                    rem_1[0] = i

                # If second occurrence
                elif rem_1[1] == -1:
                    rem_1[1] = i

        if rem_1[0] != -1 and rem_1[1] != -1:
            return print_result(l, len(l), rem_1[0], rem_1[1])

    # If remainder is '2', we have to delete either
    # one element of remainder '2' or two elements
    # of remainder '1'
    elif remainder == 2:
        rem_2 = [0]*2
        rem_2[0] = -1; rem_2[1] = -1

        # traverse array elements
        for i in range(len(l)):

            # store first element of remainder '2'
            if l[i] % 3 == 2:
                return print_result(l, len(l), i)

            if l[i] % 3 == 1:

                # If this is first occurrence of remainder 1
                if rem_2[0] == -1:
                    rem_2[0] = i

                # If second occurrence
                elif rem_2[1] == -1:
                    rem_2[1] = i

        if rem_2[0] != -1 and rem_2[1] != -1:
            return print_result(l, len(l), rem_2[0], rem_2[1])

    return 0

print(solution([5,5]))
