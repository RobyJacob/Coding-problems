def countDuplicate(numbers):
    # Write your code here
    freq = {}
    for number in numbers:
        if number in freq:
            freq[number] += 1
        else:
            freq[number] = 1

    duplicate_values = []
    for val, count in freq.items():
        if count > 1:
            duplicate_values.append(val)

    return len(duplicate_values)

print(countDuplicate([1, 3, 1, 4, 5, 6, 3, 2]))
