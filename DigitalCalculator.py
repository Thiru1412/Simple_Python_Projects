def printnum(k,arr,l):
    while(k<l):
        print(arr[k],end=" ")
        k=k+3
    print()
def calculator(a,b,o):
    if(o=='+'):
        return a+b
    elif(o=="-"):
        return a-b
    elif(o=="*"):
        return a*b
    elif(o=='/'):
        return a//b
    elif(o=='%'):
        return a%b
    elif(o=='^'):
        return a**b


def printfl(l):
    if 'a' in l:
        return (" _ ")
    else:
        return "   "
def printsl(l):
    if 'f' in l and 'g' in l and 'b' in l:
        return ("|_|")
    elif 'f' in l and 'g' in l:
        return ("|_ ")
    elif 'f' in l and 'b' in l:
        return ("| |")
    elif 'b' in l and 'g' in l:
        return (" _|")
    elif 'f' in l:
        return ("|  ")
    elif 'g' in l:
        return (" _ ")
    else:
        return ("  |")
def pritntl(l):
    if 'e' in l and 'd' in l and 'c' in l:
       return ("|_|")
    elif 'e' in l and 'd' in l:
        return ("|_ ")
    elif 'e' in l and 'c' in l:
        return ("| |")
    elif 'd' in l and 'c' in l:
        return (" _|")
    elif 'e' in l:
        return ("|  ")
    elif 'd' in l:
        return (" _ ")
    else:
        return "  |"

d={'0':'abcdef','1':'bc','2':'abged','3':'abcdg','4':'fgbc','5':'afgcd','6':'acdefg','7':'abc','8':'abcdefg','9':'abcdfg'}
print("Enter the calculation need to be done (Eg : 10 + 4) : ")
n=input()
o="+-*/%^"
i=0
while(n[i] not in o):
    i=i+1
x=n[:i]
y=n[i+1:]
a=int(n[:i])
b=int(n[i+1:])
l=[]
res=calculator(a,b,n[i])
l.append(str(res))
f=[]
for i in l:
    for j in i:
        if(j.isalnum()):
            letters=d[j]
            f.append(printfl(letters))
            f.append(printsl(letters))
            f.append(pritntl(letters))
j=0
while(j<3):
    printnum(j,f,len(f))
    j=j+1
