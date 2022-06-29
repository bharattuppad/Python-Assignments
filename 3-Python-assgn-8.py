#start parttern 1
'''
*

**

***

****
'''

#code for pattern 1
'''
for i in range(4):
    for j in range(i+1):
        print('*', end=' ')
    print('\n')
'''
#o/p:
'''
= RESTART: E:/Users/Bharat/AppData/Local/Programs/Python/Python310/python programs/3-Python-assgn-8.py
* 

* * 

* * * 

* * * *
'''
===========================================================================

#start parttern 2
'''
****

***

**

*
'''

#code for pattern 2
'''
for i in range(4):
    for j in range(4-i):
        print('*', end=' ')
    print('\n')
'''
#o/p:
'''
= RESTART: E:/Users/Bharat/AppData/Local/Programs/Python/Python310/python programs/3-Python-assgn-8.py
* * * * 

* * * 

* * 

*
'''
===========================================================================
#start parttern 3
'''
*

**

***

****

***

**

*
'''

#code for pattern 3
'''
for i in range(4):
    for j in range(i+1):
        print('*',end=' ')
    print('\n')

for k in range(3):
    for l in range(3-k):
        print('*',end=' ')
    print('\n')
'''
#o/p:
'''
= RESTART: E:/Users/Bharat/AppData/Local/Programs/Python/Python310/python programs/3-Python-assgn-8.py
* 

* * 

* * * 

* * * * 

* * * 

* * 

* 
'''
