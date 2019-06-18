years=int(input("Enter year to be checked:"))
if(years%4==0 and years%400==0):
    print("The year is a leap year!)
else:
    print("The year isn't a leap year!)
