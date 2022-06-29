#Bharat Tuppad
#QSN
'''
Develop a calculator using functions and perform all the operation on it. 

Note: The program should not terminate unless user wishes to do so.
'''

#CODE:

def calculator():
    while True:
        print('do you want to perform calculations ? type y for yes and n for no...')
        req=input()
        print('\n')
        
        if req.upper()=='Y':
            print('---------------------------------------------')
            print('calculator function is selected \n')
            a=int(input('enter the first number: '))
            b=int(input('enter the second number: '))
            print('---------------------------------------------')
            print('\n')
            add=a+b
            print('addition of the entered two numbers is: ',add)
            print('\n')
            sub=a-b
            print('subtraction of the entered two numbers is: ',sub)
            print('\n')
            mul=a*b
            print('multiplication of the entered two numbers is: ',mul)
            print('\n')
            div=a/b
            print('division of the entered two numbers is: ',div)
            print('\n')
            exp=a**b
            print('power of the entered two numbers is: ',exp)
            print('\n')
            rem=a%b
            print('remainder of the division of the entered two numbers is: ',rem)
            print('\n')
            fdiv=a//b
            print('integer part of the quotient of division of the entered two numbers is: ',fdiv)
            print('\n')
            print('---------------------------------------------')
            
        elif req.upper()=='N':
            print('thank you for using the calculator. the calculator function is closing')
            break

        else:
            print('invalid entry.. please enter the correct option')
            
        


calculator()









