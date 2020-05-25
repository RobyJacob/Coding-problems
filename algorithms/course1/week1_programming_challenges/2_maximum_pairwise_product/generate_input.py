with open("input.txt", "w") as file:
    n = 2 * 10 ** 5

    file.write(str(n) + "\n")

    arr = [str(i) + "\n" for i in range(2, n+2)]

    file.writelines(arr)
