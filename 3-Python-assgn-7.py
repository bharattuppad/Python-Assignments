#Check if a year is a leap year or not

while(True):
    print("========================================================")

    n=int(input("Enter the year to be checked: "))

    print("========================================================")

    if n<100:
        if n%4==0:
            print("It is a leap year")
        else:
            print("It is not a leap year")

    elif n>100 and n%100!=0:
        if n%4==0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        if n%400==0:
            print("It is a leap year")
        else:
            print("It is not a leap year")

'''   
there r 3 conditions for checking a leap year:

1) 2 digit year shoudl be divisble by 4
2) more than 2 digit and not a century year should be divisble by 4
3) more than 2 digit and a century year should be divisible by 400
'''
