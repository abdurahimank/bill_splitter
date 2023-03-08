# Stage 1/4: Invite your friends
no_people = int(input("Enter the number of friends joining (including you):\n"))
if no_people <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    people = [input() for i in range(no_people)]
    bill = dict.fromkeys(people, 0)
    print("\n", bill, sep="")
