print('Mahek Joshi   C081   60004220108\n')

#conversion(a)  add(x,y)  twoc(a)  right_shift(ac,q,q1)

def conversion(a):
    q=""
    current_n=len(a)
    temp=count-current_n
    if(current_n!=count):
        q="0"*temp+a
    return q

def add(x,y):
    max_length=max(len(x),len(y))
    result=''
    carry=0
    for i in range(max_length-1,-1,-1):
        r=carry
        if(x[i]=="1"):
            r+=1
        if(y[i]=="1"):
            r+=1
        if r%2==1:
            result="1"+result
        else:
            result="0"+result
        if r<2:
            carry=0
        else:
            carry=1
    return result

def twoc(a):
    l=list(a)
    for i in range(len(l)):
        if(l[i]=="1"):
            l[i]="0"
        else:
            l[i]="1"
    b="0"*(len(l)-1)+"1"
    return add("".join(l),b)


def right_shift(ac,q,q1):
    a=ac[0]
    for i in range(1,len(ac)):
        a=a+ac[i-1]
    b=ac[-1]
    for j in range(1,len(q)):
        b=b+q[j-1]
    c=q[-1]

    return a,b,c

#Input
x=int(input("enter the multiplicand"))
y=int(input("enter the multiplier"))
a=bin(x).replace("0b","")
b=bin(y).replace("0b","")
negative_a=0
negative_b=0
if(a[0]=="-"):
    a=a.replace("-","")
    negative_a=1
if(b[0]=="-"):
    b=b.replace("-","")
    negative_b=1

if(len(a)>len(b)):
    count=len(a)+1
else:
    count=len(b)+1
count1=count

firstP=conversion(a)
secondP=conversion(b)
firstN=twoc(firstP)
secondN=twoc(secondP)

AC=conversion("0")
Q1="0"

if negative_a==0:
    M=firstP
    M2=firstN
else:
    M=firstN
    M2=firstP

if negative_b==0:
    Q=secondP
else:
    Q=secondN



print("count"+" "*count1+"AC"+" "*count1+"Q"+" "*count1+"Q1"+" "*count1+"Operation")
print(str(count)+" "*count1+AC+" "*count1+Q+" "*count1+Q1+" "*count1+"Initial")
print("\n")

while(count>0):
    compare=Q[-1]+Q1
    if(compare[0]==compare[-1]):
        AC,Q,Q1=right_shift(AC,Q,Q1)
        Op="right shift"
    elif(compare=="10"):
        AC=add(AC,M2)
        AC,Q,Q1=right_shift(AC,Q,Q1)
        Op="AC=AC-M and right shift"
    elif(compare=="01"):
        AC=add(AC,M)
        AC,Q,Q1=right_shift(AC,Q,Q1)
        Op="AC=AC+m and right shift"
    print(str(count)+" "*count1+AC+" "*count1+Q+" "*count1+Q1+" "*count1+Op)
    print("\n")
    count=count-1
answer=AC+Q
if(negative_a==negative_b):
    ans_d=str(int(answer,2))
else:
    ans_d="-"+str(int(twoc(answer),2))

print("the answer in binary is ",answer)
print("the answer in decimal is ",ans_d)