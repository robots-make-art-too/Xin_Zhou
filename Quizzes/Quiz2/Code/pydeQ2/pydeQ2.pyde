# Quiz 2 - XIN ZHOU

import classList

relation = True
twoParents = False
robots = []
heads = []
g2 = [0]*5
g3 = []
def setup():
    size(600,600)
    img = loadImage('back.jpg') 
    background(img)
    loadList()
    #--------------------(name,clothcolor,headtype,pattern,relate,parent)
    grandma = classList.oldBot(robots[0],100,heads[0])
    g2[0] = classList.the2(robots[1],int(random(0,5))*50,heads[1],int(random(1,4)),False,twoParents,classList.oldBot)
    setOtherBots()        
    
def draw():
    for i in range (len(g3)):
        g3[i].flash()


def loadList():
    with open('nameList.txt','r') as f:
        for line in f:
            robots.append(line.strip())
    with open('headList.txt','r') as f:
        for line in f:
            heads.append(line.strip())
            
            
def setOtherBots():
    twoParents = True
    for i in range(1,len(g2)):  
        clothcolor = int(random(0,5)) *50  
        classList.the2.x=classList.the2.x+120
        g2[i] = classList.the2(robots[i+1],clothcolor,heads[i+1],int(random(1,4)),relation,False,classList.oldBot)
        # grandchild
        if heads[i+1]=='b':
            # g3 start from 6 in robots and heads lists
            c=int(random(0,5)) *50  
            for t in range(2):
                # parents and childs do not have same color clothes
                while c==clothcolor:
                    c=int(random(0,255))
                if len(g3)==0:
                    posX=classList.the3.x
                else :
                    posX=120+g3[len(g3)-1].x
                g3.append( classList.the3(robots[6],c,heads[6],int(random(1,4)),relation,twoParents,classList.the2,posX))
                robots.pop(6)
                heads.pop(6)
            twoParents = False

def mousePressed():
    save('FamilyPortrait.png')
