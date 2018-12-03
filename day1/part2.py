sum=0
lista = []

with open("input_test.txt") as f:
    for line in f:
        sum += int(line)
        if sum in lista:
            print sum
            break 
        lista.append(sum)
        #print lista
