
print("welcome to the Tip 💰 calculator")

Total_bill = float(input("What was the total bill (Rs.) : "))

print(f"The total bill is: {Total_bill}")

Tip=int(input("What percentage tip would you like to give ? EX: 10 12 15 : "))

People = int(input("Enter the number of people to split bill : "))

Bill_with_tip = Tip / 100 * Total_bill + Total_bill
tip_percent=Tip/100
total_tip_amount = Total_bill * Tip


print(Bill_with_tip)

Bill_per_person = Total_bill / People

final_bill=round(Bill_per_person, 2)

print(f"Each person should pay : Rs. {final_bill}")
