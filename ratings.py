"""Restaurant rating lister."""

# put your code here
file = open('scores.txt', 'r')
f = file.readlines()

newList = []
for line in f: 
    newList.append(line[:-1])
    newList.sort()

a_dictionary = {}
a_file = newList
for line in a_file:
    key, value = line.split(":")

    a_dictionary[key] = value

for key, value in a_dictionary.items():
    print(f"{key} has a {value} star rating")

user_resturaunt = input("Enter your resturaunt name...")
user_score = input("Enter the score of the previously mentioned resturaunt ...")

a_dictionary.update({str(user_resturaunt): str(user_score)})

for key, value in a_dictionary.items():
    print(f"{key} has a {value} star rating")