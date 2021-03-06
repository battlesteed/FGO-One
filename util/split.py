from PIL import Image
from config import screenshot_path


def init():  # split the screenshot in half
    im2 = Image.open(f"./{screenshot_path}")
    img2_size = im2.size
    st_x = (img2_size[1] / 9) * 16
    gap = (img2_size[0] - st_x) / 2
    left = gap
    right = img2_size[0] - gap
    top = (img2_size[1] / 2) - 100
    bottom = img2_size[1]
    # print((left, top, right, bottom))
    region = im2.crop((left, top, right, bottom))
    region2 = im2.crop((left, 0, right, top + 100))
    region.save("./temp/out.png")
    region2.save("./temp/np.png")


def main():  # split the five order cards
    im = Image.open("./temp/out.png")
    img_size = im.size
    xx = 5
    yy = 1
    x = img_size[0] // xx
    y = img_size[1] // yy
    for j in range(yy):
        for i in range(xx):
            left = i*x
            up = y*j
            right = left + x
            low = up + y
            region = im.crop((left, up, right, low))
            region.save(f"./temp/{i}.png")


def extra_split():  # get templates of servants
    for i in range(5):
        im2 = Image.open(f"./temp/{i}.png")
        img2_size = im2.size
        x = img2_size[0] / 5
        y = img2_size[1] / 7
        region = im2.crop((2 * x, 2 * y, 3 * x, 3 * y))
        region.save(f"./temp/s{i}.png")


def np_split():
    im = Image.open("./temp/np.png")
    img_size = im.size
    xx = 5
    yy = 1
    x = img_size[0] // xx
    y = img_size[1] // yy
    for i in range(1, 4):
        left = i * x
        up = y / 5
        right = left + x
        low = y
        region = im.crop((left, up, right, low))
        region.save(f"./temp/np{i-1}.png")


def split():
    init()
    main()
    extra_split()
    np_split()
