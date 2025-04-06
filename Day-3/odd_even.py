"""
--> Ask user to enter some input
--> if the number entered by user is even then print even else print odd
"""

print("Hey, welcome to the odd_even check game")
number=int(input("Enter the number of your choice : "))

if (number % 2 == 0):
    print(f"The entered number {number} is even")
else:
    print(f"The entered number {number} is odd")


print("Thanks 🙏 for using our odd_even check program, Have a good day")

