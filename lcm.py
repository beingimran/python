n1=int(input())
num = n1
rev=0

while num !=0:
    reminder=num%10
    rev=rev*10+reminder
    num/=10

if rev == n1:
    print("palindro")
else:
    print("not palindrom")

