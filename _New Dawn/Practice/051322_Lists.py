from tabulate import tabulate

# Practice file for Lists, Tuples and Dictionary

# Names of my birth family members
names_1 = ["Dad", "Mum", "Jummy", "Jolly", "Bukky", "Tolly", "Tobby"]

# Names of immediate family members
names_2 = ["Iblog", "Tolly", "Eman", "Taliya"]

# Names of my husbands family members
names_3 = ["G.Dad", "G.Mum", "Kimi", "Iblog", "Jebe", "Sly", "MOG", "Sisi Eko" ]

# Names of some of my friends
names_4 = ["Ally", "Korex", "Barakat", "salome", "Tayo"]

names = names_1.__add__(names_2)

print(names_1, names_2, names_3, names_4, names, sep="\n\n")

# Why am I unable to reassign another variable name to the function below?
# e.g ext_fam = names_1.extend(names_2)
names_1.extend(names_2)
print(names_1)

# make another lists with subset with that contains birthdays of each person
names_birthday_1 = [["Dad", "Mum", "Jummy", "Jolly", "Bukky", "Tolly", "Tobby"], ["07/10", "02/22", "05/20", "03/28", "07/22", "06/14", "03/18"]]

print(names_birthday_1)
print(" ")
print(tabulate(names_birthday_1, headers=["A 1", "A 2", "A 3", "A 4", "A 5", "A 6", "A 7"]))

# next step, complete the date of birth for the other names in this project
# Create a new file named dictionary....., make a dictionary as follow
# Nigerian states and Capital Provinces in Canada and their respective mayors




