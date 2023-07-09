select=int(input("select operations from 1,2,3,4:"))
n1=int(input("enter first number"))
n2=int(input("enter second number"))

if select==1:
    print(n1,"+",n2,"is" ,n1+n2)
elif select ==2:
    print(n1,"-",n2,"is" ,n1-n2)
elif select ==3:
    print(n1,"*",n2,"is" ,n1*n2)
elif select==4:
    print(n1,"/",n2,"is" ,n1/n2)
else:
    print("invalid choice")