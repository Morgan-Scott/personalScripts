import random

def tib(lib):
    x=random(2)
    for i in range(x+1):
        lib.pop(0)
    while(true):
        a=lib.pop(0)
        if(a="win"):
            return win
        elif(a=casc):

        elif(a="hit"):
             return hit
        elif(a="land"):
            continue
        elif(a="whiff"):
            return "whiff"
        else:
            return "error"
            
   

def createLib(casc, win, hit, land, whiff):
    lib=[]
    for i in range (casc):
        lib.append ("casc")
    for i in range (win):
        lib.append ("win")
    for i in range (hit):
        lib.append ("hit")
    for i in range (land):
        lib.append ("land")
    for i in range (whiff):
        lib.append ("whiff")
    for i in range (4):
        lib.append ("tib")
    random.shuffle(lib)
    return lib

def casc(lib)
    return lib

 
 
