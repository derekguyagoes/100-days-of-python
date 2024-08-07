with open("./file1.txt") as f:
    f1 = [i for i in f.readlines()]

with open("./file2.txt") as f:
    f2 = [i for i in f.readlines()]

result = [int(item) for item in f1 if item in f2]

print(result)

# : Result should be [3, 6, 5, 33, 12, 7]
