def exor_add(n,prev):
    if(n==prev):
        return 0
    else:
        return 1
    
def getdec(n):
    s=0
    c=0
    for i in n[::-1]:
        s=s+(int(i)*(2**c))
        c=c+1
    return s
def DecToBcd(n):
    result=[]
    while(n>0):
        result.append(n%2)
        n=n//2
    for i in result[::-1]:
        print(i,end="")
def BcdToDec(n):
    s=0
    c=0
    for i in n[::-1]:
        s=s+(int(i)*(2**c))
        c=c+1
    print("Decimal Equivalent of ",end="")
    for i in n:
        print(i,end="")
    print(" is %.0f"%s)
def BcdToGrey(n):
    result=[]
    prev=0
    for i in n:
        result.append(exor_add(int(i),prev))
        prev=int(i)
    print("Grey Value of",end=" ")
    for i in n:
        print(i,end="")
    print(" is ",end="")
    for j in result:
        print(j,end="")

def GreyToBcd(n):
    result=[]
    prev=0
    for i in n:
        prev=exor_add(int(i),prev)
        result.append(prev)
    print("Binary value of ",end="")
    for i in n:
        print(i,end="")
    print("is ",end="")
    for j in result:
        print(j,end="")
def BcdToE3(n):
    result=[]
    num=getdec(n)
    num=num+3
    DecToBcd(str(num))

print("\n1.Decimal To BCD\n2.BCD To Decimal\n3.BCD To Grey\n4.Grey To BCD")
n=int(input("Enter Your Choice : "))
if(n==1):
    num=int(input("Enter the Decimal Number : "))
    DecToBcd(num)
elif(n==2):
    num=input("Enter the Binary Number : ")
    BcdToDec(num)
elif(n==3):
    num=input("Enter the Binary Value : ")
    BcdToGrey(num)
elif(n==4):
    num=input("Enter the  Grey value : ")
    GreyToBcd(num)
elif(n==5):
    num=input("Enter the Binary value : ")
    BcdToE3(num)