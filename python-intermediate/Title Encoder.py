file = open("/usercode/files/books.txt", "r")



txt=file.read()
b=txt.replace("\n"," ")
g=b.split(" ")
str=""
for i in g:
     str+=i[0]

print(str)






file.close()