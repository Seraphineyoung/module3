
def factorialize (num):
    
    a = 1
    
    for i in range(1,num+1):
        if num == 0:
            continue
        else:
            a = i * a
    return a        
                

print(factorialize(10))


def ab (str):
    wordlen = ''
    