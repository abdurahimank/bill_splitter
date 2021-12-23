import random


num_people = int(input("Enter the number of friends joining (including you):"))
if num_people <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    people = {f"{input()}": 0 for _ in range(num_people)}
    print()
    bill_value = int(input("Enter the total bill value:"))
    print()
    lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    # to find random lucky person among friends
    if lucky_feature == "Yes":
        lucky_person = random.choice(list(people.keys()))
        print(f"\n{lucky_person} is the lucky one!")
        num_people -= 1
    else:
        lucky_person = None
        print("\nNo one is going to be lucky")
    # To find how much each should pay.
    for item in people:
        if item == lucky_person:
            people[item] = 0
        else:
            people[item] = round((bill_value / num_people), 2)
    print()
    print(people)
