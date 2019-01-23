################################# Task 1 ################################
print('What\'s you name')
age = input()

#OR

age = input('whats your name')


################################# Task 2 ################################

print('whats your age')

age = int(input())

type(age)


################################# Task 3 ################################

option = input('please input yes or no').lower()


################################# Task 4 ################################
option = input('Please input name between 1 and 5 letters').lower()


    
if len(option) in range(1,6):
    print(option)

else:
    print('Please input name between 1 and 5 letters' )
    
################################# Task 5 ################################

print('***choice***') 
print('1.Display my name') 
print('2. Display my age')
print('3. Display my city')


choice = 0

#this puts it in a loop

while True:
    
#   choice = int(input('What is your choice? '))
    
    
   while choice < 1 or choice > 3:
       choice = int(input('what is your choice again? '))
    
       if choice == 1:
            print('Ms Wu')
            
        
       elif choice == 2:
            print('5 years old')
            
        
       elif choice == 3:
            print('London')
   break

    
  ################################# Task 6 ################################  
    
print('***choice***') 
print('1.Display my name') 
print('2. Display my age')
print('3. Display my city')


choice = 0

#this puts it in a loop

while True:
    try:
       while choice < 1 or choice > 3:
           choice = int(input('what is your choice again? '))
           
           if choice == 1:
               print('Ms Wu')
        
           elif choice == 2:
               print('5 years old')
        
           elif choice == 3:
               print('London')      
       break
    except ValueError:
         print('Please enter a number')
         

  
 ################################# Task 7 ################################        
    
class Spam(object):
    def __init__(self,description,value):
        if not description or value <= 0:
           raise ValueError 
           
        self.description = description
        self.value = value
        

s = Spam('s',5)

p = Spam('b',1)

print(p.value)



class Spam1 (object):
    def __init__(self,description,value):
        assert description != ''
        assert value > 0
        self.description = description
        self.value = value



seraphine = Spam1('girl',1)

#this is goint to raise an assertion error
#seraphine = Spam1('',-1)

print(seraphine.description)






















