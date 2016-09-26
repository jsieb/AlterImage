import os, sys, getopt
from PIL import Image, ImageDraw
from random import randint

#adds a green ellipse to a random section of each image in the given directory
#then resaves over that image with the modified one
def addLeaf(filename):
    for files in os.listdir(filename):
        im = Image.open(filename + "\\" + files)
        #takes into account the size of the image -- should be a square of size (31,31)
        x,y = im.size
        #This was chosen to be small enough not to block the entire sign
        eX, eY = 7,3
        #generate a random value to begin leaf placement
        randNum = randint(5,x)
        #place leaf somewhere in image -- not alwasy completely on the sign
        bbox =  (randNum/2-eX/2, randNum/2 -eY/2, randNum/2 + eX/2, randNum/2 + eY/2)
        draw = ImageDraw.Draw(im)
        #the ellipse was chosen over square, because it is a simple shape that is more leaf-like
        draw.ellipse(bbox,  fill='green')
        del draw
        im.save(filename + "\\" + files)
        im.show()
    print "done"

def main(argv):
    #grabs the input path to use in addLeaf
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            inputfile = arg
    addLeaf(inputfile)

if __name__ == "__main__":
    main(sys.argv[1:])