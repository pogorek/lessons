# 19 MANIPULATING IMAGES

#! Computer Image Fundamentals

# ? Colors and RGBA Values

# from PIL import ImageColor
# print(ImageColor.getcolor('red', 'RGBA'))
# # (255, 0, 0, 255)
# ImageColor.getcolor('RED', 'RGBA')
# # (255, 0, 0, 255)
# ImageColor.getcolor('Black', 'RGBA')
# # (0, 0, 0, 255)
# ImageColor.getcolor('chocolate', 'RGBA')
# # (210, 105, 30, 255)
# ImageColor.getcolor('CornflowerBlue', 'RGBA')
# # (100, 149, 237, 255)

# ? Coordinates and Box Tuples

#! Manipulating Images with Pillow

from PIL import Image
# catIm = Image.open('zophie.png')
# print(catIm)
# # <PIL.PngImagePlugin.PngImageFile image mode=RGB size=816x1088 at 0x7FB7E88894C0>

# ? Working with the Image Data Type

# catIm = Image.open('zophie.png')
# print(catIm.size)
# # (816, 1088)
# width, height = catIm.size
# print(width)
# # 816
# print(height)
# # 1088
# print(catIm.filename)
# # 'zophie.png'
# print(catIm.format)
# # 'PNG'
# print(catIm.format_description)
# # 'Portable network graphics'
# catIm.save('zophie.jpg')

# im = Image.new('RGBA', (100, 200), 'purple')
# im.save('ch19_purpleImage.png')
# im2 = Image.new('RGBA', (20, 20))
# im2.save('ch19_transparentImage.png')

# ? Cropping Images

# from PIL import Image
# catIm = Image.open('zophie.png')
# croppedIm = catIm.crop((335, 345, 565, 560))
# croppedIm.save('ch19_cropped.png')

# ? Copying and Pasting Images onto Other Images

# from PIL import Image
# catIm = Image.open('zophie.png')
# catCopyIm = catIm.copy()

# faceIm = catIm.crop((335, 345, 565, 560))
# print(faceIm.size)
# # (230, 215)
# catCopyIm.paste(faceIm, (0, 0))
# catCopyIm.paste(faceIm, (400, 500))
# catCopyIm.save('ch19_pasted.png')

# catImWidth, catImHeight = catIm.size
# faceImWidth, faceImHeight = faceIm.size
# catCopyTwo = catIm.copy()
# for left in range(0, catImWidth, faceImWidth):
#     for top in range(0, catImHeight, faceImHeight):
#         print(left, top)
#         catCopyTwo.paste(faceIm, (left, top))
# # 0 0
# # 0 215
# # 0 430
# # 0 645
# # 0 860
# # 0 1075
# # 230 0
# # 230 215
# # --snip--
# # 690 860
# # 690 1075
# catCopyTwo.save('ch19_tiled.png')

# ? Resizing an Image

# from PIL import Image
# catIm = Image.open('zophie.png')
# width, height = catIm.size
# quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
# quartersizedIm.save('ch19_quartersized.png')
# svelteIm = catIm.resize((width, height + 300))
# svelteIm.save('ch19_svelte.png')

# ? Rotating and Flipping Images

# from PIL import Image
# catIm = Image.open('zophie.png')
# catIm.rotate(90).save('ch19_rotated90.png')
# catIm.rotate(180).save('ch19_rotated180.png')
# catIm.rotate(270).save('ch19_rotated270.png')

# catIm.rotate(6).save('ch19_rotated6.png')
# catIm.rotate(6, expand=True).save('ch19_rotated6_expanded.png')

# catIm.transpose(Image.FLIP_LEFT_RIGHT).save('ch19_horizontal_flip.png')
# catIm.transpose(Image.FLIP_TOP_BOTTOM).save('ch19_vertical_flip.png')

# #? Changing Individual Pixels

# from PIL import Image
# im = Image.new('RGBA', (100, 100))
# print(im.getpixel((0, 0)))
# # (0, 0, 0, 0)
# for x in range(100):
#     for y in range(50):
#         im.putpixel((x, y), (210, 210, 210))

# from PIL import ImageColor
# for x in range(100):
#     for y in range(50, 100):
#         im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
# print(im.getpixel((0, 0)))
# # (210, 210, 210, 255)
# print(im.getpixel((0, 50)))
# # (169, 169, 169, 255)
# im.save('ch19_putPixel.png')

#! Project: Adding a Logo


#! Drawing on Images
# TODO
