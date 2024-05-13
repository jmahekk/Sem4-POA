print('Mahek Joshi   C081   60004220108\n')

block_size=[100,500,200,300,600]
block_size1=[100,500,200,300,600]
block_size2=[100,500,200,300,600]

process=[]
n=int(input("enter the number of processes: "))
for i in range(0,n):
    size=int(input(f"enter the size for process P{i}: "))
    process.append(size)

print(process)

#first fit
pro=[]
occ=[]
for i in process:
    for j in block_size:
        if(i<=j):
            occ.append(j)
            block_size.remove(j)
            pro.append(i)
            break

c=len(pro)
com_uti=0
for i in range(0,c):
    print(f"{pro[i]}          {occ[i]}")

for i in pro:
    com_uti=com_uti+i

com_uti=(com_uti/1700)*100
print(f"percentage utilised for first fit is {com_uti}")

#best fit
occ=[]
pro=[]
for i in process:
    best=-1
    for j in block_size1:
        if(i<=j):
            if(best==-1):
                best=j
            elif (best>j):
                best=j
                
    if(best!=-1):
        occ.append(best)
        block_size1.remove(best)
        pro.append(i)

c=len(pro)
com_uti=0
for i in range(0,c):
    print(f"{pro[i]}      {occ[i]}")
for i in pro:
    com_uti=com_uti+i

com_uti=(com_uti/1700)*100
print(f"percentage utilised for first fit is {com_uti}")


#worstfit
pro=[]
occ=[]
block_size2.sort(reverse=True)
for i in process:
    for j in block_size2:
        if(i<=j):
            occ.append(j)
            block_size2.remove(j)
            pro.append(i)
            break

c=len(pro)
for i in range(0,c):
    print(f"{pro[i]}     {occ[i]}")
com_uti=0
for i in pro:
    com_uti=com_uti+i
com_uti=(com_uti/1700)*100
print(f"percentage utilised for first fit is {com_uti}")