result=[]
A=1
B=1
i=0
while A!=0 and B!=0:
    A,B= map(int,input().split())
    if A==0 and B==0:
        break
    result.append(A+B)
    print(result[i])
    i+=1
