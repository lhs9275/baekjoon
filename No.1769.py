### my code ###
   time over
   
x = int(input())
x_len = len(str(x))
count,total = 0,0
element=[]
result=1
while True :

    while x_len>0:
        main = 10**(x_len-1)
        x_1 = x//main
        x= x-(main*x_1)
        element.append(x_1)
        x_len-=1
        count+=1
        
    for  i in range (count):
        total= total+ element[i]
        i+=1
        
    if total<10:
        print(result)
        if total%3==0:
            print("YES")
        else:
            print("NO")
        break
    else:
        result +=1
        x=total
        x_len = len(str(x))
        count,total = 0,0
        element=[]



________________________________________________________________________________________________________________________________________________________________________________________
good



num = input()
cnt = 0

while len(num)>1:
    cnt+=1
    answer=0
    for i in num:
        answer+=int(i)
    num = str(answer)
    
print(cnt)

if int(num)%3 ==0:
    print("YES")
else:
    print("NO")

    
    
 



        
