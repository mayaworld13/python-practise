#write the program to print first n odd natural number

def n_odd_natural_number(n) :
    for i in range(n):
        print(2*i+1)
        
n = int(input("Enter the number of odd number you want :"))

n_odd_natural_number(n)