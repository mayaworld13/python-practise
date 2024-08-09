# write the python script for find the square of first n natural number

def square_of_n_natural_no(n) :
    for i in range(1,n) :
        print(i**2, end=" ")
        
        
n = int(input("Enter the count of natural number that you want to be squared: "))

square_of_n_natural_no(n)