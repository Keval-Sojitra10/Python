def powers(n):
    l1 = []
    for i in range(1,n+1):
        l1.append((i,i*i,i*i*i))
    print(l1)
       
x = int(input("Enter number:"))
powers(x)
    
