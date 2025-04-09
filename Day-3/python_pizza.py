"""
--> write a pizza Delivery program

Based on a user's order. work out their final bill. Use the input() fuction to get a user's preferences and then add total for their order and tell them how much they have to pay

small size (s): $15
Medium pizza (M): $20
large Pizza (L): $25

Add pepernoi for small pizza (Y or N) : +$2
Add perperoni for medium or large pizza (Y or N): +$3
Add extra cheese for my size pizza (Y or N): +$1

"""

print("Welcome to the pizza delivery !")
pizza_type=input("What size pizza do you want ? S, M or L: ")
perperone_request=input("Do you want perperoni on your pizza: Y or N : ")
cheese_request=input("Do you want extra cheese ? Y or N ")
bill = 0

if pizza_type == "S" :
    bill += 15
elif pizza_type == "M" :
    bill +=20
elif pizza_type == "L" :
    bill +=25
else:
    print("you typed wrong size, please type only S/M/L ")


if perperone_request == "Y" :
    if pizza_type == "S":
        bill += 2
    else:
        bill += 3


if cheese_request == "Y":
    bill += 1

print(f"your final bill is : ${bill}.")
