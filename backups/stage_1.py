# Project: Bill Splitter
# Stage 1/4: Invite your friends
no_friends = int(input("Enter the number of friends joining (including you):\n"))
if no_friends <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    friends = [input() for i in range(no_friends)]
    bill = dict.fromkeys(friends, 0)
    print(bill)
