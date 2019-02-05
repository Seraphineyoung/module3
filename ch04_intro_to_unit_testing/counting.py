#import time
#
#
#list = ['hello']
#new_list=[]
#for item in list:
#    
#    for character in item:
#        new_list.append(character)
#        print(new_list[(new_list.index(character))])
#        time.sleep(.40)
#    
#    list_length = len(new_list)
#    
#    for i in range((len(new_list))):
#        del(new_list[list_length-1])
#        list_length -=  1
#        print(new_list)
#    
    

#def F():
#    a,b = 0,1
#    while True:
#        yield a
#        a, b = b, a 

#for i in range(1,51):
#    
#    print(i)
    

#for i in range(1,51):
#    mylist.append(i)
#print(mylist)
    

#fibList=[0,1]



#def fib_func (n):
#    i = 0
#    for z in range(n):
#        a = fibList[i]
#        b = fibList[i+1]
#        x = a+b
#        fibList.append(x)
#       
#        i = i+ 1
#    print(fibList[(len(fibList))-1])
#
##fib_func(20)

#
def fib_gen (n):
    a = 1
    b = 1
    for i in range(n): 
        yield a  
        a, b = b ,b + a
        print(a,b)
        
     
for num in fib_gen(20):
    print(num)











        