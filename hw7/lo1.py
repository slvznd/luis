class Matrix:

    def __init__(self, list_1):
        self.list_1 = list_1

    def __add__(self, other):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        for i in range(len(self.list_1)):
            for j in range(len(other.list_1[i])):
                matr[i][j] = self.list_1[i][j] + other.list_1[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.list_1]))


my_matrix_1 = Matrix([[5, 18, 11],
                      [6, 17, 23],
                      [41, 50, 9]])

my_matrix_2 = Matrix([[45, 8, 2],
                      [6, 7, 93],
                      [24, 5, 97]])
print(my_matrix_1 + my_matrix_2)