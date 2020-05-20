def groupSort(arr):
    # Write your code here
    from collections import Counter
    import operator

    freq = dict(Counter(arr))

    matrix = [[] for i in range(len(freq))]

    for idx, key in enumerate(freq):
        matrix[idx].append(key)
        matrix[idx].append(freq[key])

    matrix.sort()
    matrix.sort(key=operator.itemgetter(1), reverse=True)

    print(matrix)


groupSort([3, 3, 1, 2, 1])
