# Project: Bill Splitter
# Stage 2/4: The bill has arrived
no_friends = int(input("Enter the number of friends joining (including you):\n"))
if no_friends <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    friends = [input() for i in range(no_friends)]
    total_bill = float(input("\nEnter the total bill value:\n"))
    bill = dict.fromkeys(friends, round(total_bill / no_friends, 2))
    print("\n", bill, sep="")
