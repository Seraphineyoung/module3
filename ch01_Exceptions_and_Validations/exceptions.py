
##################### TASK 1 ####################

try:
    f = open('testfile.txt')
    
except Exception:
    print('Error!')
    
##################### TASK 2 ####################
    
try:
    f = open('testfile.txt')
    s1 = not_exist

except FileNotFoundError:
    print('Sorry, this file does not exist, or the file name is wrong. Please double check')
except Exception:
    print('Sorry. Something went wrong after opening function')
    
 

#################### TASK 3 ##################### 
    
try:
    f = open('testfile.txt')
    s1 = not_exist

except Exception as e:
    print(e)
    
################### TASK 4 ##################### 
    
try:
    f = open('testfile.txt')

except Exception as e:
    print(e)
    
else:
    print(f.read())
    f.close()
 
#the else block clause will be executed if he try block does not raise an exception.
    

################### TASK 5 #####################
    
try:
    f = open('testfile')
    
except Exception as e:
    print(e)
    
else:
    print(f.read())
    f.close()
    
finally:
    print('executing finally....')
    
#################### OR #####################    
    
try:
    f = open('testfile.txt')
    
except Exception as e:
    print(e)
    
else:
    print(f.read())
    f.close()
    
finally:
    print('executing finally....')
    
    
################### TASK 6 #####################
    
try:
    f = open('testfile.txt')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    