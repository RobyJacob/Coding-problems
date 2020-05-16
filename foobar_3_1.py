import fractions
from fractions import Fraction
from functools import reduce

def gcd(x, y):
    def gcd1(x, y):
        if y == 0:
            return x
        return gcd1(y, x%y)
    return gcd1(abs(x), abs(y))

def transform(mat):
    Q, R, sum_of_states, terminal_idx = [], [], [], []

    # sum over column, to get sum of states
    sum_of_states = list(map(sum, mat))

    # index of terminal or absorbing states
    terminal_idx = list(map(lambda x: x == 0, sum_of_states))

    # number of terminal states
    total_term_states = sum(terminal_idx)

    # divide each state by the sum of states to get corresponding probabilities
    for i in range(len(mat)):
        mat[i] = list(map(lambda x: Fraction(0, 1) if sum_of_states[i] == 0 else Fraction(x, sum_of_states[i]), mat[i]))

    # put all transients states together and absorbing states together
    transform_mat = []
    for i in range(len(mat)):
        transform_mat.append([])
        expand_mat = []
        for j in range(len(mat)):
            if not terminal_idx[j]:
                transform_mat[i].append(mat[i][j])
            else:
                expand_mat.append(mat[i][j])
        transform_mat[i].extend(expand_mat)

    # split matrix into Q and R
    for i in range(len(transform_mat)):
        if not terminal_idx[i]:
            Q.extend([transform_mat[i][:len(transform_mat)-total_term_states]])
            R.extend([transform_mat[i][len(transform_mat)-total_term_states: ]])

    return {"Q": Q, "R": R, "term_states": terminal_idx, "num_term_states": total_term_states}

def inverse(m):
    identity_mat = []

    # create identity matrix of same shape as m
    for i in range(len(m)):
        identity_mat.append([int(i == j) for j in range(len(m))])

    # matrix of which inverse need to be found
    mat = []
    for i in range(len(m)):
        mat.extend([[identity_mat[i][j]-m[i][j] for j in range(len(m))]])

    # augment identity matrix to mat
    for i in range(len(mat)):
        mat[i].extend(identity_mat[i])

    # elementary row operation
    # R(i+1) = R(i+1) - R(i)*temp
    for i in range(len(mat)):
        for j in range(len(mat)):
            if j != i:
                temp = mat[j][i] / mat[i][i]
                for k in range(len(mat[0])):
                    mat[j][k] -= (mat[i][k]*temp)

    # divide diagonal elements by itself to form identity matrix
    for i in range(len(mat)):
        temp = mat[i][i]
        for j in range(len(mat[0])):
            mat[i][j] /= temp

    # extract inverse matrix from augmented matrix
    inv = []
    for i in range(len(mat)):
        inv.extend([mat[i][len(mat):]])

    return inv

def mat_mul(a, b):
    result_mat = []

    for i in range(len(a)):
        result_mat.extend([[Fraction(0,1)]*len(b[0])])
        for j in range(len(b[0])):
            val = Fraction(0,1)
            for k in range(len(b)):
                val += a[i][k] * b[k][j]
            result_mat[i][j] = val

    return result_mat

def format(arr):
    # calculate lcm for denominator
    lcm = 1
    for i in range(len(arr)):
        lcm = (lcm*arr[i].denominator) / gcd(lcm, arr[i].denominator)

    # store numerators
    res = list(map(lambda x: int(x.numerator*lcm / x.denominator), arr))

    # append denominator
    res.append(lcm)

    return res

def solution(m):
    # dictionary of Q, R and absorbing states
    cache = transform(m)

    # edge case when m is empty
    if cache["num_term_states"] == len(m):
        return [1, 1]

    # fundamental matrix
    N = inverse(cache["Q"])

    # txr matrix where (i,j) is the number of times a transient state transitions to absorbing state
    R = cache["R"]

    #absorbing probabilities
    B = mat_mul(N, R)

    return format(B[0])


print(solution([[1,2]]))
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
