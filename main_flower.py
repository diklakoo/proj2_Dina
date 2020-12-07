list=[]
flowers = {}
file= open("iris.data",'r')
for line in file :
    l = line.rstrip().split(",")
    if len(l) == 5 :
        height = l[3]
        name = l[4]
        if name in flowers:
            flowers[name] = round(float(flowers[name]) + float(height), 2)
        else:
            flowers[name] = height

def printing_flower_height(dict):
 for key in dict:
    print ( key,dict[key])

printing_flower_height(flowers)

