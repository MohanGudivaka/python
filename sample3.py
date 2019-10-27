import sympy as s
n=int(input())
count=0
for i in range(n,20):
	if s.isprime(i):
		print(i)
		count=-1
		break
