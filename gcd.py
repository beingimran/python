n1=int(input())
n2=int(input())

if n1 > n2:
    temp = n1
    n1= n2
    n2=n1

for i in range(1,n1):
    if n1%i==0 and n2%i==0:
         hcf=i
       

print(hcf)