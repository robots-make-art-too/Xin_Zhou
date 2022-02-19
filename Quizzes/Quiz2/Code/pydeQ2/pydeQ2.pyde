# Quiz 2 - XIN ZHOU

import classList

robots = []
g1Num= g2Num=0
gener1 = [0]*g1Num
gener2 = [0]*g2Num
gener3 = []

def setup():
    size(600,600)
    img = loadImage('back.jpg') 
    background(img)
    loadList()#(Generations,Name,HeadType,TwoParents,childNum,Spause,hasChild)     
    getRobs()
def draw():
    for i in range (len(gener3)):
        gener3[i].flash()


def loadList():
    global g1Num, g2Num,g3Num
    with open('nameList.txt','r') as f:
        for line in f.readlines():
            robots.append(line[:-1].split('#'))
    for i in range (len(robots)):# get Num of each generation
        if robots[i][0]=='1': 
            g1Num = g1Num+1
        elif robots[i][0]=='2':
            g2Num = g2Num+1

def getRobs(): #name,clothcolor,headtype,pattern,relate(mom),twoParents,parentName
     global g1Num, g2Num,g3Num
#gener1-----------------------------------------------------------------------------------------
     for i in range(g1Num):
         gener1.append (classList.oldBot(robots[i][1],100,robots[i][2]))
#gener2-----------------------------------------------------------------------------------------         
         clothcolor = int(random(0,4)*60)
         t = 0
         childNum = int(robots[i][4])
         countChild = 0
         c = setCololor(clothcolor)
         while t <childNum:
            gener2.append(classList.the2(robots[g1Num+t][1],c,robots[g1Num+t][2],int(random(1,4)),robots[g1Num+t][5],False,classList.oldBot))
#gener3-----------------------------------------------------------------------------------------        
            clothcolor = setCololor(clothcolor)
            for n in range (countChild,int(robots[g1Num+t][4])+countChild):
                if len(gener3)==0:
                    posX=classList.the3.x
                else :
                    posX=120+gener3[len(gener3)-1].x
                gener3.append(classList.the3(robots[g1Num+g2Num+n][1],clothcolor,robots[g1Num+g2Num+n][2],int(random(1,4)),robots[g1Num+g2Num+n][5],robots[g1Num+g2Num+n][3],classList.the2,posX))
                countChild= countChild+1
            classList.the2.x = classList.the2.x + 120   
            if robots[g1Num+t][6]=='True':
                t = t+1
                gener2.append(classList.the2(robots[g1Num+t][1],int(random(0,255)),robots[g1Num+t][2],int(random(1,4)),robots[g1Num+t][5],False,classList.oldBot))
                classList.the2.x = classList.the2.x + 120
                childNum = childNum + 1
            t = t +1
            
def setCololor(parColor): #be sure don't have same color with mom
    childColor = int(random(0,4)*60)   
    while parColor == childColor:
        childColor = int(random(0,4)*60)
    return childColor      
                                                                    
def mousePressed():
    save('FamilyPortrait.png')
