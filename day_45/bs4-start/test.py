from bs4 import BeautifulSoup

with open("./website.html", "r") as site:
    contents = site.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all("a")
for tag in all_anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

company_url = soup.select_one(selector="#name")
# print(company_url)

headings = soup.select(".heading")
print(headings)
