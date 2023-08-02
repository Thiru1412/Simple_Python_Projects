def or_add(n,prev):
    if(n==1 or prev==1):
        return 1
    else:
        return 0

def exor_add(n,prev):
    if(n==prev):
        return 0
    else:
        return 1

def invert(n):
    if(n==1):
        return 0
    if(n==0):
        return 1
def AND_GATE(table):
    result=[]
    for row in table:
        temp=1
        for j in row:
            temp=temp*j
        result.append(temp)
    print("A . B")
    print()
    for i in result:
        print(i)

def OR_GATE(table):
    result=[]
    for row in table:
        prev=0
        for j in row:
            prev=or_add(j,prev)
        result.append(prev)
    print("A + B")
    print()
    for i in result:
        print(i)

def NOT_GATE(table):
    result=[]
    for row in table:
        for i in row:
            result.append(invert(i))
    print("_")
    print("A")
    print()
    for j in result:
        print(j)

def NAND_GATE(table):
    result=[]
    for row in table:
        temp=1
        for i in row:
            temp=temp*i
        result.append(invert(temp))
    print("_____")
    print("A . B")
    print()
    for j in result:
        print(j)

def NOR_GATE(table):
    result=[]
    for row in table:
        prev=0
        for i in row:
            prev=or_add(i,prev)
        result.append(invert(prev))
    print("_____")
    print("A + B")
    print()
    for j in result:
        print(j)

def EXOR_GATE(table):
    result=[]
    for row in table:
        prev=0
        for i in row:
            prev=exor_add(i,prev)
        result.append(prev)
    print("_     _")
    print("AB + AB")
    print()
    for j in result:
        print(j)

def EXNOR_GATE(table):
    result=[]
    for row in table:
        prev=0
        for i in row:
            prev=exor_add(i,prev)
        result.append(invert(prev))
    print("_______")
    print("_     _")
    print("AB + AB")
    for j in result:
        print(j)
def IMPLEMENT_GATE(gate,table):
    if(gate=="AND"):
        AND_GATE(table)
    elif(gate=="OR"):
        OR_GATE(table)
    elif(gate=="NOT"):
        NOT_GATE(table)
    elif(gate=="NAND"):
        NAND_GATE(table)
    elif(gate=="NOR"):
        NOR_GATE(table)
    elif(gate=="EXOR"):
        EXOR_GATE(table)
    elif(gate=="EXNOR"):
        EXNOR_GATE(table)



print("\n1.AND\n2.OR\n3.NOT\n4.NAND\n5.NOR\n6.EXNOR\n7.EXNOR\n")
gate=int(input("Enter Your Choice : "))
n=int(input("\nEnter Number of Inputs : "))
col=2**n
pin=65
table=[]
row=[]
for i in range(n):
    print(chr(pin),end=" ")
    pin=pin+1
print()
for i in range(col):
    row=list(map(int,input().split()[:n]))
    table.append(row)
    for j in row:
        if(j!=0 and j!=1):
            print("Values Should be Either 0 or 1 .")
            exit(0)
print()
if(gate==1):
    IMPLEMENT_GATE("AND",table)
elif(gate==2):
    IMPLEMENT_GATE("OR",table)
elif(gate==3):
    IMPLEMENT_GATE("NOT",table)
elif(gate==4):
    IMPLEMENT_GATE("NAND",table)
elif(gate==5):
    IMPLEMENT_GATE("NOR",table)
elif(gate==6):
    IMPLEMENT_GATE("EXOR",table)
elif(gate==7):
    IMPLEMENT_GATE("EXNOR",table)
else:
    print("Enter Valid Choice !!!")