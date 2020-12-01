'''d = []
with open("iris.data") as f:
    for line in f:
       d = [line]'''

list=[]
file= open("iris.data",'r')
for line in file :
    list.append(line.split(","))

sum=0
for i in list:
    list[0][0]= int(list[0][0])


print (list[0][0])



