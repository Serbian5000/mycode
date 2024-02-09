#!/usr/bin/env python3

"""A program to ask if you can fly"""

# Ask if user can fly
answer = input("Can you fly? (yes/no/hmmm... maybe): ")

# if 'no', respond "that's expected"
if answer == "no":
    print('That\'s expected!')

# if 'yes', respond "wow!"
elif answer == 'yes':
    print('Wow!')

# if 'I don't know' respond "DON\'T TRY!"
else:
    print("DON\'T TRY!!!")
