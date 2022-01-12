try:    
    a = int(input("Enter a:"))    
    b = int(input("Enter b:"))    
    c = a/b  
    print("a/b = %f"%c)    
except Exception:    
    print("can't divide by zero")    
    print(Exception)  
else:    
    print("Hi I am else block")    
