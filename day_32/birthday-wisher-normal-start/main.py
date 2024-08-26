import datetime as dt
import os
import pandas
import random as random


def emailer(letter_to_send):
    print(letter_to_send)


today = (dt.datetime.now().month, dt.datetime.now().day)

bdays = pandas.read_csv("./birthdays.csv")

birthdays_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in bdays.iterrows()
}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    letters = os.listdir("./letter_templates")
    random_letter = random.choice(letters)
    with open(f"./letter_templates/{random_letter}", "r") as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        emailer(contents)
else:
    print("no")
