
class Calculator(object):
    
    
    def add(self,x,y):
        try:
            return (x + y)
    
        except:
            print('please enter a number')
        
    
sera = Calculator()

print(sera.add("a", 1))