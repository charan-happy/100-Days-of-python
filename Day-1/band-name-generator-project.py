"""
Band name Generator project
------------------------------
Description :

1. Create a  greeting for your program
2. Ask the user for the city that they grew up in and store it in a variable
3. Ask the user for a name of a pet and store it in a variable
4. combine the name of their city and pet and show them their band name
5. Make sure the input is always in title case (e.g. "new york" => "New York")
6. Make sure the input cursor shows on the new line
"""

print("Welcome to the Band Name Generator!")
print("Let's find out your band name!")
print("--------------------------------------------------")
city = input("Please type the city you grew up in:\n")
print("--------------------------------------------------")
pet=input("Please type the name of your pet:\n")
print("--------------------------------------------------")
band_name = city.title() + " " + pet.title()
print("Your band name could be: " + band_name)

print("--------------------------------------------------")
print("Thanks for using the Band Name Generator!")

