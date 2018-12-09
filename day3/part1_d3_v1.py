import numpy
import re


def extract_info(line):
    j = re.findall("\d+", line)
    j = map(int, j)
    x,y,w,h = j[1], j[2], j[3], j[4]
    return x,y,w,h

def fill_matrix(file_path):
    matrix = numpy.zeros((10,10))
    with open(file_path) as f:
        for line in f:
            x,y,w,h = extract_info(line)
            for j in range(y,y+h):
                for i in range(x, x+w):
                    if matrix[i][j] == 1:
                        matrix[i][j] = 8
                    else:
                        matrix[i][j] = 1
    return matrix

def count_Xs(matrix):
    #...

    return num_Xs

matrix = fill_matrix('input.txt')
print matrix

# num_Xs = count_Xs(matrix)
# print num_Xs
