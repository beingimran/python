n=int(input())


if n==0 and n==1:
    print("not prime")
else:
    for i in range(2,n/2):
        if n%2==0:
            print("is not prime")

            break

        else:
             print("prime")




