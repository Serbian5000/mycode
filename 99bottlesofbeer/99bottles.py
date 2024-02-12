#!/usr/bin python3


"""Write a for loop of 99 bottles of beer"""


for i in range(99, 0, -1):
    print(f"{i} bottles of beer on the wall!")
    print(f"{i} bottles of beer! Take one down, pass it around.")
    if i == 1:
        print("no more bottles of beer on the wall!")

    else:
        print(f"{i - 1} bottles of beer on the wall!")

    print()
