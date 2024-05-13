print('Mahek Joshi   C081   60004220108\n')

def binary(a):
    bits_list=[]
    while a>0:
        num=a
        b=int(num%2)
        bits_list.append(b)
        num=num//2
        a=int(a/2)
    bits_list.reverse()
    return bits_list

def shift(shiftA,shiftQ):
    val=shiftA+shiftQ
    l=len(val)
    i=0
    for i in range(0,l-1):
        val[i]=0
        val[i]=val[i+1]
    del val[i]
    return val


def compliment(value):
    onecomp=[]
    twocomp=[]
    for i in range(0,len(value)):
        if(value[i]==0):
            onecomp.append(1)
        elif(value[i]==1):
            onecomp.append(0)

    carry=1
    for j in range(len(value)-1,-1,-1):
        if(onecomp[j]==0 and carry == 1):
            twocomp.append(1)
            carry=0
        elif(onecomp[j]==1 and carry == 1):
            twocomp.append(0)
            carry=1
        elif(onecomp[j]==0 and carry == 0):
            twocomp.append(0)
            carry=0
        elif(onecomp[j]==1 and carry==0):
            twocomp.append(1)
            carry=0
    twocomp.reverse()
    return twocomp

def Add(valA,valM):
    add=[]
    ad=valA
    carry=0
    for i in range(len(ad)-1,-1,-1):
        if(valA[i]==0 and valM[i]==0 and carry==0):
            add.append(0)
            carry=0
        elif(valA[i]==0 and valM[i]==0 and carry==1):
            add.append(1)
            carry=0
        elif(valA[i]==0 and valM[i]==1 and carry==0):
            add.append(1)
            carry=0
        elif(valA[i]==0 and valM[i]==1 and carry ==1 ):
            add.append(0)
            carry=1
        elif(valA[i]==1 and valM[i]==0 and carry==0):
            add.append(1)
            carry=0
        elif(valA[i]==1 and valM[i]==0 and carry==1):
            add.append(0)
            carry=1
        elif(valA[i]==1 and valM[i]==1 and carry==0):
            add.append(0)
            carry=1
        elif(valA[i]==1 and valM[i]==1 and carry==1):
            add.append(1)
            carry=1
    add.reverse()
    return add

def decimal(bin):
    bin.reverse()
    dec=0
    for i in range(0,len(bin)):
        if(bin[i]==1):
            dec=dec+(bin[i]*(2**i))
        elif(bin[i]==0):
            pass
    bin.reverse()
    return dec

dividend=int(input("enter the value of dividend Q: "))
divisor=int(input("enter the value of divisor M: "))

q=binary(dividend)
m=binary(divisor)

print("Q: ",*q)

if (len(m)<=len(q)):
    diff=len(q)-len(m)
    for i in range(0,diff+1):
        m.insert(0,0)

print("M: ",*m)

ACC=[]
for i in range(0,len(m)):
    ACC.append(0)

print("ACC: ",*ACC)

negM=compliment(m)
print("-M: ",*negM)

print("")
print("        ","    |    ","     A     ","    |    ","    Q     ","    |    ")
n=1

counter=len(q)

while counter>0:
    a=shift(ACC,q)
    newA=a[0:len(ACC)]
    newQ=a[len(ACC):]
    sumAM=Add(newA,negM)

    b=len(newQ)+1
    if(sumAM[0]==1):
        newQ.insert(b,0)
        sumAM=Add(sumAM,m)
    elif(sumAM[0]==0):
        newQ.insert(b,1)
    

    ACC=sumAM
    q=newQ
    print("step: ",n,"    |    ",*ACC,"     |     ",*q,"    |    ")
    n=n+1
    counter=counter-1

print("remainder: ",decimal(ACC))
print("quotient: ",decimal(q))