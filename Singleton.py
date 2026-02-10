def singleton(arg):       #using List
    L=[]
    def inner():
        if len(L)==0:
            obj=arg()
            L.append(obj)
        return L[0]
    return inner
@singleton
class sample:
    def __init__(self):
        print('Executed') 
obj1= sample()
print(obj1)
obj2= sample()
print(obj2)

output: Executed
        <__main__.sample object at 0x0000020BE9427320>
        <__main__.sample object at 0x0000020BE9427320>
      
        
