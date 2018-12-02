from PIL import Image
def blend_two_image():
    base_img = Image.open("human.jpg")
    hat_img = Image.open("hat.png")
    

    target = Image.new("RGBA", base_img.size, (0,0,0,0))

    x1 = 250
    y1 = 50
    x2 = 430
    y2 = (187*(x2-x1)+256*y1)//256

    box = (x1,y1,x2,y2)
    region = hat_img.convert("RGBA")
    region = region.resize((box[2]-box[0], box[3]-box[1]))

    target.paste(base_img,(0,0))
    target.paste(region,box,region)

    target.show()
    target.save("blend.png")

blend_two_image()

