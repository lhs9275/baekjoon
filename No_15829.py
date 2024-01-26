L = int(input())
S = list(map(str,input()))
s=0
for i in range(L):
    s =s+(ord(S[i])-96)*(31**i)
print(s%1234567891)



mod는 나머지라는 뜻.
a mod b 는 a%b
