## compare two images, return a number
import sys

from PIL import Image as pil

def GrayScale():
    # src directory is current directory
    # dst directory is current_directory/images
    for image in glob.glob("*.jpeg"):
        myimage = pil.open(image)

        grey = myimage.convert('L') ### convert to grey-scale
        grey=np.asarray(grey,dtype=np.uint8)  #if values still in range 0-255!
        w=pil.fromarray(grey,mode='L') ### convert back to image
        outfilename = os.path.splitext(os.path.basename(image))[0]+'_grey.jpeg'
        w.save(outfilename)

    return 0

def CompareImages(m1, m2):

    # if it is same, return 0; otherwise, return a positive number
    # if there is an error, return -1
    mm1 = pil.open(m1)
    mm2 = pil.open(m2)
    width, height = mm1.size
    width2, height2 = mm2.size
    if (width!=width2 or height!=height2):
        return -1
    #print width, height

    pix1=mm1.load()
    pix2=mm2.load()


    #mse = ((p1 - p2) ** 2).mean(axis=None)
    #print mse

    bin = [0] * 256
    #bin = []

    #for k in range(0, 256):
    #    bin.append(0)

    total = 0
    total_n = 0
    total_1 = 0
    total_2 = 0
    for i in range(0, width):
            for j in range(0, height):

                bin[pix1[i,j]] += 1
                total += (pix1[i,j] - pix2[i,j])**2
                #total_n += (pix1[i,j])**2
                total_1 += (pix1[i,j])
                total_2 += (pix2[i,j])
                #if (i%1000==0 and j%1000==0):
                    #print i, j, pix1[i,j], pix2[i,j], total, total_n
    #print total
    #total = long(total)/long(width*height)
    #f1 = long(0.0) + long(total_n)/long(total)

    f1 = total
    #*long(width*height)

    f2 = long(total_1)*long(total_2)
    #print f1
    #print f2
    f2 = f2/f1
    f2 = f2/1000000

    #print total
    return f2
