# Project: Bill Splitter
# Stage 4/4: Party is over
import random


no_friends = int(input("Enter the number of friends joining (including you):\n"))
if no_friends <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    friends = [input() for i in range(no_friends)]
    total_bill = float(input("\nEnter the total bill value:\n"))
    lucky_feature = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky_feature == "Yes":
        lucky = random.choice(friends)
        bill = dict.fromkeys(friends, round(total_bill / (no_friends - 1), 2))
        bill[lucky] = 0
        print(f"{lucky} is the lucky one!")
    else:
        bill = dict.fromkeys(friends, round(total_bill / no_friends, 2))
        print("No one is going to be lucky")
    print("\n", bill, sep="")
