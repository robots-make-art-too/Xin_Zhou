import random
from PIL import Image, ImageDraw, ImageFont

methods=['boil','fry','deep fry']
meat = ['pork','chicken','beef']
veg=['garlic','broccli','apple']
drink=['tea','soda','orange juice']
backColor = []


#build image
def buildImage():
    # get background
    img = Image.open('1.jpg')
    draw = ImageDraw.Draw(img)
    # set font
    font = ImageFont.truetype("arial.ttf", size=30)
    # write
    draw.text((0,0),methods[random.choice(range(3))],fill='#000000',font=font)

    #save img
    img.save('today.jpg')
    print('in')

buildImage()