#exercise 7

#Write a function to remove all the red from an image.


import image

img = image.Image("luther.jpg")
newimg = image.EmptyImage(img.getWidth(),img.getHeight())
win = image.ImageWin()

for col in range(image.getWidth()):
    for row in range(img.getHeight()):
       p = img.getPixel(col,row)

       newred = 0
       newgreen = p.getGreen() 
       newblue = p.getBlue()

       newpixel = image.Pixel(newred,newgreen,newblue)

       newimg.setPixel(col,row,newpixel)

newimg.draw(win)
win.exitonclick()
