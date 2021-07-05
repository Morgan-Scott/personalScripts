import random

def create():
    deck=[]
    curve=[36,22,18,16,0,2,0,1]
    for i in range(0,len(curve)):
        for j in range (0,curve[i]):
            deck.append([i,False])
    tracked=[0,0,2,1]
    for k in range(0,len(tracked)):
        for l in range (0,tracked[k]):
            deck.append([k,True])
    random.shuffle(deck)
    return deck
def tash(deck):
    tot=0
    lost=[]
    while tot<20:
        x=deck.pop(0)
        tot +=x[0]
        if (x[1]):
            lost.append(x[1])
    return lost

def tashtest():
    lostAgg=[0,0,0,0,0,0]
    x=0
    for i in range (0,100000):
        deck=create()
        lost=tash(deck)
        x=len(lost)
        lost=tash(deck)
        x+=len(lost)
        lost=tash(deck)
        lostAgg[len(lost)+x]+=1
    return lostAgg
        
