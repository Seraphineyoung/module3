

################################# Task 4 ################################
#option = input('Please input name between 1 and 5 letters').lower()
#
#
#    
#if len(option) in range(1,6):
#    print(option)
#
#else:
#    print('Please input name between 1 and 5 letters' )
    
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

    
    
    
        
    























