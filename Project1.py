#comment
#
#
#opening images
from PIL import Image

def medianOdd(myList):
# Store list length in the variable listLength
    listLength = len(myList)
# Sort the list
    sortedValues = sorted(myList)
# Location of middle value. Subtract one because of zero index
    middleIndex = ((listLength + 1)/2) - 1
# Return the object located at that index
    return sortedValues[middleIndex]

#lists
imgList =[]
imgList.append(Image.open("Project1Images/1.png"))
imgList.append(Image.open("Project1Images/2.png"))
imgList.append(Image.open("Project1Images/3.png"))
imgList.append(Image.open("Project1Images/4.png"))
imgList.append(Image.open("Project1Images/5.png"))
imgList.append(Image.open("Project1Images/6.png"))
imgList.append(Image.open("Project1Images/7.png"))
imgList.append(Image.open("Project1Images/8.png"))
imgList.append(Image.open("Project1Images/9.png"))

pictureWidth, pictureHeight = imgList[8].size
print pictureHeight
print pictureWidth

#Pixel lists
redPixelList =[]
greenPixelList =[]
bluePixelList =[]

#newImage
newImage = Image.new("RGB", (pictureWidth, pictureHeight))

for x in range(0, pictureWidth):
    for y in range(0,pictureHeight):
        for myImage in imgList:
            
            myRed, myGreen, myBlue = myImage.getpixel((x,y))
            
            redPixelList.append(myRed)
            greenPixelList.append(myGreen)
            bluePixelList.append(myBlue)
            
        redPixels = medianOdd(redPixelList)
        greenPixels = medianOdd(greenPixelList)   
        bluePixels = medianOdd(bluePixelList)  
        #clearing pixel lists
        redPixelList = []
        greenPixelList =[]
        bluePixelList = []
    
        newImage.putpixel((x,y),(redPixels,greenPixels,bluePixels))
    
newImage.save("newImage.png", "PNG")


    
        