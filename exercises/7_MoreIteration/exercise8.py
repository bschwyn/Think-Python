#8

#write a function to convert the image to grayscale.

# ISSUE need to figure out the whole file thing

import image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(),img.getHeight())
win = image.ImageWin()

for col in range(img.getWidth()):
    for row in range(image.getHeight()):
       p = img.getPixel(col,row)
	   
	   gray = (p.getRed()+p.getGreen()+p.getBlue())/3

       newred = gray
       newgreen = gray
       newblue = gray

       newpixel = image.Pixel(gray,gray,gray)

       newimg.setPixel(col,row,newpixel)

newimg.draw(win)
win.exitonclick()