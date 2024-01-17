### abs (절대값)를 이용해 불필요한 코드 제거 

A,B = map(int, input().split())
if A<B:
    print(abs(B-A))
else:
    print(abs(A-B))
