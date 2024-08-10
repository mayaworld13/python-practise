# write the python script to check whether the number is prime or not

def prime_or_not(number) :
    if number <=1 :
        return "not  a prime"
    elif number == 2 :
        return " prime"
    elif number > 2 and number % 2 ==0:
        return "not a prime"
    
    for i in range (3, int(number ** .5) +1, 2):
        if number % i == 0:
            return False
    else :
        return "prime"
    
number = int(input("Enter the number: "))   
print(f"{number}  is  {prime_or_not(number)} number")
