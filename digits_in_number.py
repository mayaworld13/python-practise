# write the python script to find count number of digits in a number

def count_digits(number):
    count = 0
    while number != 0:
        number //= 10  
        count += 1     
    return count

number = int(input("Enter a number: "))

print(count_digits(number))