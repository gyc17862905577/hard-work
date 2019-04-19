from PIL import Image


def black_w(route):
    img = Image.open(route)
    Img = img.convert('L')
    Img.save(r'C:\Users\Amy\Desktop\test1.jpg')

black_w(r'C:\Users\Amy\Desktop\test.jpg')