#exercise 10
#Sepia Tone images are those brownish colored images that may
#remind you of times past. The formula for creating a sepia tone is as follow:

#newR = (R × 0.393 + G × 0.769 + B × 0.189)
#newG = (R × 0.349 + G × 0.686 + B × 0.168)
#newB = (R × 0.272 + G × 0.534 + B × 0.131)

#Write a function to convert an image to sepia tone. (Hint)

# ISSUE need to figure out the whole file thing

import image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(),img.getHeight())
win = image.ImageWin()

for col in range(image.getWidth()):
    for row in range(image.getHeight()):
       p = img.agegetPixel(col,row)
	   
	   newred = 
       newgreen = gray
       newblue = gray


       newpixel = img.Pixel(newred,newgreen,newblue)

       newimg.setPixel(col,row,newpixel)

newimg.draw(win)
win.exitonclick()