import numpy
import re

N = 1000
file_path = 'input.txt'

def extract_info(line):
    j = re.findall("\d+", line)
    return map(int, j)

def fill_matrix(file_path):
    matrix = numpy.zeros((N,N))
    with open(file_path) as f:
        for line in f:
            id_num,x,y,w,h = extract_info(line)
            for j in range(y,y+h):
                for i in range(x,x+w):
                    matrix[j][i] += 1
    return matrix

def all_equals_to_one(matrix,x,y,w,h):
    for j in range(y,y+h):
        for i in range(x,x+w):
            if matrix[j][i] >= 2:
                return False
    return True

def find_no_overlap(file_path, matrix):
    with open(file_path) as f:
        for line in f:
            id_num,x,y,w,h = extract_info(line)
            if all_equals_to_one(matrix,x,y,w,h):
                return id_num
    return 'Not found'

matrix = fill_matrix(file_path)

square_id_num = find_no_overlap(file_path,matrix)
print square_id_num
