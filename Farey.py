def Fnext(Fm):
    FtoAdd = []

    for i in range(0, len(Fm)-1):
        FtoAdd.append((Fm[i][0] + Fm[i+1][0], Fm[i][1] + Fm[i+1][1]))

    result = [None] * (len(Fm) + len(FtoAdd))
    result[::2] = Fm
    result[1::2] = FtoAdd
    print('FtoAdd=', FtoAdd)

    return result

def farey(n):
    counter = 1
    Fn = [(0,1), (1,1)]
    
    while counter < n:
        counter += 1
        Fn = Fnext(Fn)
    
    return Fn

print(farey(4))