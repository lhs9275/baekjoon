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
k=0
len_word=len(word)
while k<len_word:
    print(word[k])
    k= k+1
