n=  5

for i in range(n):
    p=1
    q=1
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(q,end=" ")
        q += 1
    print()

    q= 1
    for j in range(i+1-1):
        print(p,end=" ")
        p+=1
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1-1):
        print(q,end=" ")
        q+=1
    print()