from readVentsFromFile import ventLines

withVent = set()
results = set()

for vent in ventLines:
    x1, y1 = map(int,vent[0].strip().split(','))
    x2, y2 = map(int,vent[1].strip().split(','))
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            current = "{}-{}".format(x1,i)
            if current in withVent:
                results.add(current)
            else:
                withVent.add(current)
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1,x2)+1):
            current = "{}-{}".format(i,y1)
            if str(current) in withVent:
                results.add(current)
            else:
                withVent.add(current)
    elif abs((x1-x2)/( y1-y2)) == 1:
        for i in range(abs(x2-x1)+1):
            directionx = 1 if  x2 > x1 else -1
            directiony = 1 if  y2 > y1 else -1
            current = "{}-{}".format(x1 + i * directionx, y1 + i * directiony)
            if current in withVent:
                    results.add(current)
            else:
                    withVent.add(current)


print(len(results))