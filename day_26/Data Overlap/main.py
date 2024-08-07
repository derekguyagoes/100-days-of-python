with open("./file1.txt") as f:
    f1 = [eval(i) for i in f.readlines()]

with open("./file2.txt") as f:
    f2 = [eval(i) for i in f.readlines()]

result = [item for item in f1 if item in f2]

print(result)

# : Result should be [3, 6, 5, 33, 12, 7]
