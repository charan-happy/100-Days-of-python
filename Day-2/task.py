# subscripting
"welcome" # This is a string
print("welcome"[1:3]) 
print(len("welcome[1]"))

# string
print("123" + "453")

# Integer = whole number
print(2446 + 4526)

# large integers
print(12,345,256)


print(12_345_256)

# float
print(3.5256)

# Boolean
print(True)
print(False)

## Type errors: checking and conversion

print(len("235353"))

print(type(len("2345")))

print(type("3253"))

name_of_the_user= input("enter your name : ")
length_of_the_name=len(name_of_the_user)

print(type(name_of_the_user))
print(type(length_of_the_name))
print("no.of letters in your name: "+ str(length_of_the_name))


## print my age
print("my age: " + str(23))
print(235 + 564)
print(8-2)
print(8 // 4)
print(8 / 3)
print(2 ** 3)

# PEMDASLR

BMI = 84 / 1.76 ** 2

print(BMI)

print(int(BMI))

print(round(BMI))

print(round(BMI, 2))

## f-strings

marks = 50
subject = "python"
is_passed = True

print(f"In {subject}, you got {marks}, and you passed : {is_passed}")
