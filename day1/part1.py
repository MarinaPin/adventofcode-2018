sum=0

with open("input.txt") as f:
    for line in f:
        sum += int(line)

print sum
