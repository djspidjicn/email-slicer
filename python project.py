# EMAIL SLICER PROGRAM

def slicer(e):
    # Finding Username using for loop
    u=""
    f=0
    for i in range(0,len(e)):
        if e[i]=='@':
            if i==len(e)-1:
                f+=2
                break 
            elif i==0:
                f+=3
                break
            else:
                f+=1
                break
        elif e[i]==' ':
            f+=4
            break
        u+=e[i]
    return (u,i,f)
    # Finding Username using String Slicing
    # u=e[:e.index('@')]

        
# Main program module
print("\n**************************************************************************")
print("\n\t\t\t-:EMAIL SLICER:-\n")
print("\n**************************************************************************")
n=int(input("\nEnter the number of email addresses you want to enter :"))

f=0
un=[]
dm=[]
k=0
# mu=""

for i in range(n):
    e=input(f"\nEnter the email address {i+1} : \n")
    u,k,f = slicer(e)
    if f==1:
        # Finding Domain using for loop
        # for j in range(k+1,len(e)):
        #     d+=e[j]

        d=e[e.index('@')+1:]

        # Modifying username if needed like excluding the numerical part or replacing the '.' with '_'
        # for i in u:
            # if ord(i)>=48 and ord(i)<=57:
            #     continue
            # elif i=='.':
            #     mu+='_'
            #     continue
            # mu+=i

        un.append(u)
        dm.append(d)
    elif f==2:
        # email does not have any domain
        un.append(0)
        dm.append(1)
    elif f==3:
        # email does not have any username
        dm.append(0)
        un.append(1)
    elif f==4:
        # email does not have any space in between  
        un.append(1)
        dm.append(1)
    else:
        # email does not have any '@' symbol
        un.append(0)
        dm.append(0)

        
for i in range(n):
    print(f"\nEmail {i+1} :")
    if un[i]==0 and dm[i]==0:
        print("\nPlease enter valid email address. Your email does not have any \'@\' symbol")
    elif dm[i]==0:
        print("\nPlease enter valid email address. Your email does not have any username")
    elif un[i]==1 and dm[i]==1:
        print("\nPlease enter valid email address. Email id should not have any space in between")
    elif un[i]==0 :
        print("\nPlease enter valid email address. Your email does not have any domain")
    else:
        print("\nUsername:",un[i],"& Domain:",dm[i].upper())


print("\n**************************************************************************\n")
print("Thank you for using our program.")
print("Please visit again!\n")
print("**************************************************************************")