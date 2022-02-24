import random
from PIL import Image, ImageDraw, ImageFont

methods=['Boil','Fry','Deep Fry']
meat = ['Pork','Chicken','Beef']
veg=['Garlic','Broccli','Apple']
drink=['Maple Tea','Soda','Orange Juice']
fontColor = ['#826260','#953827','#A4AA51','#AA7534','#60754E','#744644']


#build image

def buildImage():
    global img,font1,font2,draw
    # get background
    img = Image.open('1.jpg')
    draw = ImageDraw.Draw(img)
    # set font
    font1 = ImageFont.truetype("arial.ttf", size=30)
    font2 = ImageFont.truetype("arial.ttf", size=26)
    # write
    drawSentence ()
    #save img
    img.save('today.jpg')


def drawSentence ():
    draw.text((10,20),'What is you\nSupper?',fill='#D8B481',font=font1)
    draw.text((10,100),random.choice(methods),fill=random.choice(fontColor),font=font1)
    draw.text((90,140),random.choice(meat),fill=random.choice(fontColor),font=font1)
    draw.text((90,205),random.choice(veg),fill=random.choice(fontColor),font=font1)
    draw.text((10,180),'with\n\n\ndrink',fill='#D8B481',font=font2)
    draw.text((90,300),random.choice(drink),fill=random.choice(fontColor),font=font1)
