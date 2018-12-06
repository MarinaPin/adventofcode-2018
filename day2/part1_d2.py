from collections import Counter

num_letters =[]
cont_2 = 0
cont_3 = 0

#with open("day2//input.txt") as f:
with open("input.txt") as f:

    for line in f:
        c = Counter(line)
        num_letters = c.values()
        if 2 in num_letters:
            cont_2 += 1
        if 3 in num_letters:
            cont_3 +=1
print cont_2*cont_3