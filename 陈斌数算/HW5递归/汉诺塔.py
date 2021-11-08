def movetower(height,fromPloe,withPole,toPole):
    if height >=1:
        movetower(height-1,fromPloe,toPole,withPole)
        moveDisk(height,fromPloe,toPole)
        movetower(height-1,withPole,fromPloe,toPole)

def moveDisk(disk,fromPole,toPole):
    print(f'Move disk[{disk}] from {fromPole} to {toPole}')

movetower(5,"#1","#2","#3")