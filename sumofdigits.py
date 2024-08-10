# write the python script to find sum of digits in a number

def sum_of_digits_in_a_number(number) :
    
    number_string = str(abs(number))
    
    digit_sum = 0
    for digits in  number_string :
        digit_sum+=int(digits)
    return digit_sum
        

    


number = int(input("Enter the number: "))
print("sum of digits in a number", sum_of_digits_in_a_number(number), end = " ")


