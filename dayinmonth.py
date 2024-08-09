# finding the number of days in a month in particular year

year = int(input("enter the year :"))

month = int(input("enter the year in range 1 - 12 :"))

def leapyear() :
    return (year % 400 == 0 )or (year % 100 !=0 and year % 4 == 0)

def day_in_month(month, year ) :
    if month in [1,3,5,7,8,10,12] :
        return 31
    elif month == 2:
        return 29 if leapyear(year) else 28
    elif month > 12 :
        print("Invalid month number")
    else :
        return 30


days = day_in_month(month, year )
print(f"The number of days in {month}th month of year {year} is: {days}")
