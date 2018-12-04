sum=0
lista = set()
file_contents =[]
d=0

with open("input_test.txt") as f:
    for line in f:
        file_contents.append(int(line))

while d <= 0:
    for i in file_contents:
        sum += int(i)
        if sum in lista:
            print sum
            d = 1
            break
        else:
            lista.add(sum)
