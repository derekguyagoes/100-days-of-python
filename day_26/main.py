numbers = [1, 2, 3]

# new_list = [new_item for item in list]
# new_list = [new_item for item in list if test]

# new_list = [n + 1 for n in numbers]
#
# print(numbers)
# print(new_list)

# name = "Angela"
# new_list = [letter for letter in name]

# new_list = [n * 2 for n in range(1, 5)]
# new_list = [n * 2 for n in range(1, 10) if n % 2 == 0]

# print(new_list)

list_of_strings = ["9", "0", "32", "8", "2", "8", "64", "29", "42", "99"]
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n % 2 == 0]
print(result)
