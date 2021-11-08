moneytuple = tuple(map(int, input().split()))

def theif(mtup, reuselst={}):
    if mtup in reuselst:
        return reuselst[mtup]
    elif len(mtup)==1:
        reuselst[mtup]=mtup[0]
        return reuselst[mtup]
    elif len(mtup)==2:
        reuselst[mtup] = max(mtup)
        return reuselst[mtup]
    else:
        reuselst[mtup]=max(theif(mtup[:-2], reuselst) + mtup[-1], theif(mtup[:-1], reuselst))
        return reuselst[mtup]

print(theif(moneytuple))