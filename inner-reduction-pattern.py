a=4
for i in range(1,a*2):
    for j in range(1,a*2):
        x=i+j
        y=a*2
        if i>=j and i+j<=a*2:
            print(a+1-j,end=" ")
        elif i<=j and i+j<=a*2:
            print(a+1-i,end=" ")
        elif i<=j and i+j>=a*2:
            print(j-(a-1),end=" ")
        else:
            print(i-(a-1),end=" ")
    print()
