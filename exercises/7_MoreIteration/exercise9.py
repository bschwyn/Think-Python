#exercise 9
#write a function to convert an image to black and white

# ISSUE need to figure out the whole file thing

import image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(),img.getHeight())
win = image.ImageWin()

for col in range(image.getWidth()):
    for row in range(image.getHeight()):
       p = img.getPixel(col,row)
	   
	   if (p.getRed()+p.getGreen()+p.getBlue())/3 > 127:
	       newred = newgreen = newblue = 255
		else:
			newred = newgreen = newblue = 0

       newpixel = image.Pixel(newred,newgreen,newblue)

       newimg.setPixel(col,row,newpixel)

newimg.draw(win)
win.exitonclick()