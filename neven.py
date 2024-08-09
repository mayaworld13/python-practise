#write the program to print first n even natural number

def n_even_natural_number(n) :
    for i in range(1, n+1) :
        print(2*i)
      
    
n = int(input("enter the number of even number you want : ") )   

n_even_natural_number(n)