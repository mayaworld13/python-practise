# number = int(input("Enter the number :"))

# if number % 2 == 0 :
#     print("the number is even")
    
# else :
#     print("odd")

    
    
# print("even" if int(input("Enter the number :")) % 2 == 0 else "odd")



# divisibility of a number of 5


# number = int(input("Enter the number :"))

# if number % 5 == 0 :
#     print("The Number ", number, "is divisible by 5")
    
# else :
#     print("The Number ",number , "is not divisible by 5")


# print("The Number is divisible by 5" if int(input("Enter the number :")) % 5 == 0 else "The Number is not divisible by 5")





# postive negative zero
# number = float(input("Enter the number :"))

# if number > 0 :
#     print("the number is positive")

# elif number < 0 :
#     print("the number is negative")

# else :
#     print("the number is zero")
    
# print("the number is positive" if (number := float(input("Enter the number :"))) > 0 else "the number is negative" if  number < 0 else "the number is zero")


# a= int(input("Enter first number:"))
# b= int(input("Enter second number:"))
# c= int(input("Enter third number:"))

# if a > b and a > c :
#     print("A is greater than all")
    
# elif b > c and b > a :
#     print(" B is greater than all")

# else :
#     print("C is greater than all")


# print("A is greater than all" if (a > b and a > c) > 0 else " B is greater than all" if  (b > c and b > a) < 0 else "C is greater than all")

print("Leap year" if (year := int(input("Enter the year :"))) % 400 == 0 or year % 100 !=0 and year % 4 == 0  else "not a leap year")