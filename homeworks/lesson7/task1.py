import random
"""
PEP-8
"""
"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен 
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix 
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем 
с первым элементом первой строки второй матрицы и т.д.
"""
# Код программы


def new_matrix(row, col):
    """Функция создает матрицу заданных размеров со случайными числами от 0 до 10
    :param row: количество строк матрицы
    :param col: количяество колонок матрицы
    :return: список длинной row со значениями состоящих из списков длиной col, где значения случайных чисел от 0 до 10
    """
    matrix = []
    inx = col
    while row:
        matrix_line = []
        while inx:
            matrix_line.append(random.randrange(0, 10))
            inx -= 1
        row -= 1
        inx = col
        matrix.append(matrix_line)
    return matrix


class Matrix:

    def __init__(self, l_matrix):
        self.matrix = l_matrix

    def __str__(self):
        row = len(self.matrix)
        x = 0
        f_str = f""
        while x < row:
            step = ""
            y = 0
            col = len(self.matrix[x])
            while y < col:
                f_str = f"{f_str}{step}{self.matrix[x][y]}"
                y += 1
                step = " "
            x += 1
            if x == row:
                f_str = f"{f_str}"
            else:
                f_str = f"{f_str}\n"
        return f_str

    def __add__(self, other):
        """Суммирует две матрицы одинакового порядка
        :return: возвращает матрицу
        """
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            row = len(self.matrix)
            x = 0
            new_row = []
            while x < row:
                col = len(self.matrix[x])
                y = 0
                new_col = []
                while y < col:
                    new_col.append(self.matrix[x][y] + other.matrix[x][y])
                    y += 1
                new_row.append(new_col)
                x += 1
            return Matrix(new_row)
        raise ValueError('Матрицы не одинакового порядка')


if __name__ == "__main__":
    matrix1 = Matrix(new_matrix(5, 4))
    matrix2 = Matrix(new_matrix(5, 4))
    print("matrix1")
    print(matrix1)
    print("matrix2")
    print(matrix2)
    matrix3 = Matrix.__add__(matrix1, matrix2)
    print("matrix3")
    print(matrix3)
