import sys

T=int(sys.stdin.readline())
N=[0 for _ in range(T)]

for i in range (T):
    N[i]=int(sys.stdin.readline())

N.sort()

for value in range(len(N)):   
    print(N[value])


### 알게된 점 
sys.stdin.readline() 이 input() 보다 빠르지만 값이 크다면 input()이 더 빠름 
리스트의 크기를 0 for _ in range(T) 같은 느낌으로 지정가능
