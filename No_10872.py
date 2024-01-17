X = int(input())
result=1
if X==0:
    print(1)
else:
    for i in range(1,X+1):
        result=i*result
    print(result)
