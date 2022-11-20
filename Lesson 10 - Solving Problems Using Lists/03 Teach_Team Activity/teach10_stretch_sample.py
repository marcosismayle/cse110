
"""
File: teach10_sample.py
Author: Brother Burton

Purpose: Practice working with parallel lists.
"""

print("Enter the names and balances of bank accounts (type: quit when done)")

names = []
balances = []

name = None

# Build the lists
while name != "quit":
    name = input("What is the name of this account? ")

    if name != "quit":
        balance = float(input("What is the balance? "))

        names.append(name)
        balances.append(balance)

# Display all of the accounts with their balances
# Compute the total at the same time.
total = 0

print("\nAccount Information:")
for i in range(len(names)):
    print(f"{i}. {names[i]} - ${balances[i]:.2f}")

    total += balances[i]

average = total / len(balances)

print()
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")

# Stretch Challenges:

# Find the highest balance:
highest_name = None
highest_balance = -1

for i in range(len(names)):
    name = names[i]
    balance = balances[i]

    if balance > highest_balance:
        # We have a new highest!
        highest_balance = balance
        highest_name = name

print(f"Highest balance: {highest_name} - ${highest_balance:.2f}")

change_account = "yes"

while change_account == "yes":
    change_account = input("\nDo you want to update an account? ")

    if change_account == "yes":
        index = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? "))

        balances[index] = new_amount
    
    # Now print the balances
    print("\nAccount Information:")
    for i in range(len(names)):
        print(f"{i}. {names[i]} - ${balances[i]:.2f}")

