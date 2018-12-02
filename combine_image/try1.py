from PIL import Image

def blend_two_image():
    img1 = Image.open("hat.png")

    img2 = Image.open("human.jpg")
    img2 = img2.convert("RGBA")

    region = img1
    region = region.convert("RGBA")

    box = (266,30,356,120)
    region = region.resize((box[2]-box[0], box[3]-box[1]))

    img2.paste(region, box, img2)
    img2.show()

    img2.save('blend.bmp')

blend_two_image()