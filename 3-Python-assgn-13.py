#Bharat Tuppad
#Assignment-13

#Question
'''
Dictionary
d = {'a':10,'b':30,'c':50,'d':100}

Q1.write a code to update the value of key 'b' to 300
output-: {'a':10,'b':300,'c':50,'d':100}

Q2.write a code to check if key 'e' is present in dictionary d
if it 'e' is not present in d, then it should return 'e key does not exist'
output-: 'e key does not exist'

Q3.write a code to add new key,value  i.e 'e',600 respectively inside dictionary d
output-: {'a':10,'b':300,'c':50,'d':100,'e':600}

Q4.write a code to display all the values from the dictionary
output-: dict_values([10, 300, 50, 100, 600])

Q5.write a code to merge the dictionary x inside dictionry d
x = {'i':11,'j':12,'k':13,'l':14}
output-: {'a':10,'b':300,'c':50,'d':100,'e':600,'i':11,'j':12,'k':13,'l':14}

Q6.write a code to remove the key 'j' from dictionary d
output-: {'a':10,'b':300,'c':50,'d':100,'e':600,'i':11,'k':13,'l':14}
'''

#code :
d={'a':10, 'b':30, 'c':50, 'd':100}
print("Before any operation, set d is: ",d)
print('\n')
print('-----------------------------------------------------------')

#1
d.update({'b':300})
print('After operation 1: ',d)
print('\n')
print('-----------------------------------------------------------')

#2
print(d.get('e'),'e key does not exist')
print('\n')
print('-----------------------------------------------------------')

#3
d['e']=600
print(d)
print('\n')
print('-----------------------------------------------------------')

#4
print(d.values())
print('\n')
print('-----------------------------------------------------------')

#5
x={'i':11, 'j':12, 'k':13, 'l':14}
print('Dictionary x is: ',x)
print('\n')
d.update(x)
print('after merging dicitonary x, d becomes: ',d)
print('\n')
print('-----------------------------------------------------------')

#6
d.pop('j')
print('after removing j, dictionary d becomes: ',d)














