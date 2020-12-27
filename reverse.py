n=int(input())
revno=0

while n != 0 :
    reminder=n%10
    revno=revno*10+reminder
    n=n/10

print(revno)