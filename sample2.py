import sympy
T=int(input())
while(T!=0):
    n=int(input())
    for i in range(n+1,20):
    	count=0
        if sympy.isprime(i):
            if((i^n)>n):
            	print(i)
            	count+=1
            	break
    if count==0:
    	print(-1)
   	for i in range(n+1,10):
    	count=0
        if(sympy.isprime(i)):
            if((i^n)<n):
            	print(i)
            	count+=1
            	break
    if count==0:
    	print(-1)
    for i in range(n+1,10):
    	count=0
        if(!sympy.isprime(i)):
            if((i^n)>n):
            	print(i)
            	count+=1
            	break
    if count==0:
    	print(-1)

    for i in range(n+1,10):
    	count=0
        if(!sympy.isprime(i)):
            if((i^n)<n):
            	print(i)
            	count+=1
            	break
    if count==0:
    	print(-1)
            
    T-=1
