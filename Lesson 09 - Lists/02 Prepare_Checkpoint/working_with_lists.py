
"""
File: workin_with_lists.py
Author: Marcos Ismayle

Purpose: Practice using lists, by adding the names of friends.
"""

friends = []
new_friend = ''
print()
while new_friend != 'end':
    new_friend = input('Type the name of a friend: ')
    friends.append(new_friend)
print()
print(f'Your friends are:')
print()
for friend in friends[:-1]:
    
    print(friend)

print()