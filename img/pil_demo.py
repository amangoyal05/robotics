# https://pillow.readthedocs.io/en/stable/reference/Image.html

from PIL import Image, ImageFilter
import os

# Opening the image
image1 = Image.open('01-cat-Adult.jpeg')
image1.show()

# Saving the image in a different format
image1.save('01-cat-Adult.png')

# Saving multiple images in a different format
for f in os.listdir('.'):
    if f.endswith('.jpeg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        print(fn)
        i.save(f'pngs/{fn}.png')

# Resizing images
size_300 = (300, 300)                          #(y, x)
size_700 = (700, 700)

for f in os.listdir('.'):
    if f.endswith('.jpeg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.thumbnail(size_300)
        i.save(f'300/{fn}_300{fext}')
        i.thumbnail(size_700)
        i.save(f'300/{fn}_700{fext}')

# Rotating image
image1.rotate(90).save('01-cat-Adult_rotate.jpeg')

# Black and white
image1.convert(mode='L').save('01-cat-Adult_bnw.jpeg')

# Blurring the image
image1.filter(ImageFilter.GaussianBlur(radius=10)).save('01-cat-Adult_blur.jpeg')
# Radius the degree of blurriness