# # fileNotFound
#
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as msg:
#     print(f"no: {msg}")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("done")
#

fruits = ["Apple", "Pear", "Orange"]


# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit pie")


# make_pie(4)

facebook_posts = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 13, "Comments": 2, "Shares": 1},
    {"Likes": 33, "Comments": 8, "Shares": 3},
    {"Comments": 4, "Shares": 2},
    {"Comments": 1, "Shares": 1},
    {"Likes": 19, "Comments": 3},
]


def count_likes(posts):
    total_likes = 0
    for post in posts:
        try:
            total_likes = total_likes + post["Likes"]
        except KeyError:
            pass
    return total_likes


print(count_likes(facebook_posts))
