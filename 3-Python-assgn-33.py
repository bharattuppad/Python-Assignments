#Bharat Tuppad
#QSN
'''
Create a dictionary
account = {"balance":10000,"pin":1234}
perform functions like
1) Withdraw money and store the updated dictionary in a file (Serialization)
2) Load the file (Deserialization) and check balance
'''
#CODE-

acc_det={"balance":10000,"pin":1234}
d=acc_det['balance']
e=acc_det['pin']

def withdraw():
    
    while True:
        print('\nenter the pin to withdraw or enter q to quit the transaction\n')
        a=input('enter the pin: ')
        
        if a=='1234':
            print('------------------------------------------------')
            print('\ncurrent balance: ',d)
            b=int(input('\nenter the amount to be withdrawn: '))
            rem=d-b
            print('\n****Kindly collect your cash from the dispenser and card from the slot...****')
            print('\nremaining balance: ',rem)
            print('\ntransaction successfull')
            print('------------------------------------------------')
            f={"balance":rem}
            return rem
            
        elif a.lower()=='q':
            print('------------------------------------------------')
            print('Transaction cancelled.. exiting the request..')
            print('------------------------------------------------')
            break

        else:
            print('\ninvalid pin')
            print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

    
h=withdraw()
print(h)
g={"balance":h}
acc_det.update(g)
print(acc_det)


import pickle

abc=('available balance is: ',acc_det['balance'])

z=open("assgn-33.pickle","wb")
pickle.dump(abc,z)
z.close()


y=open("assgn-33.pickle","rb")
obj = pickle.load(y)
print(obj)


