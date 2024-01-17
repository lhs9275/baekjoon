word =[]
how_many = int(input())
for  i in range(how_many):
    a = input()
    if a in word:
      pass
    else:
      word.append(a)
    i=i+1
word.sort()   
word.sort(key=len)

for i in range (how_many):
    print(word[i])
    i= i+1
