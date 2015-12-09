import array

a = [[12.14 , 12.3] , 1,2,3,4,5,"'teste'"]
b= a[0]
print(a)
print(b)
print (len(b))
print('-----------------------------------------')

for a1 in a:    
    if isinstance(a1, list):
        for a2 in a1:
            print(a2)
    else:
        print(a1)    
           
print('-----------------------------------------')
 
for i in range(10):
    print(i)
    
enum =  ["ENJM1","ENUM2"]


for i, x in enumerate(enum):
    print(i,x)      
    
    
def somar(a,b=9):
    return a+b 

print(somar(2, b=9))
print (type(range(2)))

from datetime import date as d1
d = (2015,1,1)
print(d1(*d))

