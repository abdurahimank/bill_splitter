# Stage 4/4: Party is over
import random


no_people = int(input("Enter the number of friends joining (including you):\n"))
if no_people <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    people = [input() for i in range(no_people)]
    bill_value = int(input("\nEnter the total bill value:\n"))
    lucky_option = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky_option == "Yes":
        lucky = random.choice(people)
        print(f"\n{lucky} is the lucky one!")
        bill = {i: round(bill_value / (no_people - 1), 2) if i != lucky else 0 for i in people}
    else:
        print("\nNo one is going to be lucky")
        bill = dict.fromkeys(people, round(bill_value / no_people, 2))
    print("\n", bill, sep="")
