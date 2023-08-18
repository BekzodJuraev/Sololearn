
text = input()
dict = {}
sum=0
total=0
for i in text:

    sum+=len(i)
    #dict[i] = sum
    if text.count(i) >1:
        dict[i] = text.count(i)
    else:
        sum = 0
        dict[i] = sum



for i in dict:
    if dict[i]==0:
        sum=1
        dict[i]=sum



print(dict)


