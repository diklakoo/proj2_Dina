
def Cumulative_height():
    flowers = {}
    file = open("iris.data", 'r')
    for line in file:
        l = line.rstrip().split(",")
        if len(l) == 5:
            height = l[3]
            name = l[4]
            if name in flowers:
                flowers[name] = round(float(flowers[name]) + float(height), 2)
            else:
                flowers[name] = height
    return flowers

def printing_flower_height():
    flowers = Cumulative_height()
    for key in flowers:
      print ( key,flowers[key])


def main() :
    printing_flower_height()

if __name__ == '__main__':
    main()



