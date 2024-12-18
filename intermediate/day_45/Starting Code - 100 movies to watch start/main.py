import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
# print(response.text)
my_list = []
soup = BeautifulSoup(response.text, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.get_text() for movie in all_movies]

with open("movies.txt", "w") as file:
    for movie in movie_titles:
        file.write(movie + "\n")

print(movie_titles[::-1])
