class not2DError(Exception):
    # Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
    # Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
    # Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'

def mul1d(arr1, arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return 1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i] * arr2[i]
    return sum

class list_D2(list):
    def __init__(self, arr):
        if not all(isinstance(inner, list) and all(not isinstance(sub_inner, list) for sub_inner in inner) for inner in arr):
            raise not2DError()

        if len(set(len(inner) for inner in arr)) > 1:
            raise unevenListError()

        self.extend(arr)

    def __str__(self):
        rows = len(self)
        if rows > 0:
            cols = len(self[0])
        else:
            cols = 0
        return f'list_2D: {rows}*{cols}'

    def transpose(self):
        transposed = [[self[i][j] for i in range(len(self))] for j in range(len(self[0]))]
        return list_D2(transposed)

    def __matmul__(self, other):
        if len(self[0]) != len(other):
            raise improperMatrixError()

        result = []
        other_transposed = other.transpose()
        for row in self:
            result.append([mul1d(row, col) for col in other_transposed])
        return list_D2(result)

    def avg(self):
        total_sum = sum(sum(row) for row in self)
        total_elements = sum(len(row) for row in self)
        if total_elements > 0:
            return total_sum / total_elements
        else:
            return 0.0
