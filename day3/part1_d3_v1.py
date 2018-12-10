import numpy
import re

N = 1000

def extract_info(line):
    j = re.findall("\d+", line)
    j = map(int, j)
    x,y,w,h =j[0], j[1], j[2], j[3], j[4]
    return x,y,w,h

def fill_matrix(file_path):
    matrix = numpy.zeros((N,N))
    with open(file_path) as f:
        for line in f:
            x,y,w,h = extract_info(line)
            for j in range(y,y+h):
                for i in range(x, x+w):
                    if matrix[j][i] == 1 or matrix[j][i] ==8:
                        matrix[j][i] = 8
                    else:
                        matrix[j][i] = 1
    return matrix

def count_Xs(matrix):
    n = 0
    for j in range(N):
        for i in range(N):
            if matrix[i][j] == 8:
                n += 1
    return n

matrix = fill_matrix('input.txt')

num_Xs = count_Xs(matrix)
print num_Xs