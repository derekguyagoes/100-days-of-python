import os

import helpers

helpers.delete_garb_files(f"{os.getcwd()}/Output/ReadyToSend")

with open("Input/Letters/starting_letter.txt") as file:
    letter = file.readlines()

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

for n in names:
    name = n.strip()
    with open(f"./Output/ReadyToSend/{name}", "w") as output_file:
        for line in letter:
            if "[name]" in line:
                output_file.write(line.replace("[name]", name))
            else:
                output_file.write(line)
