#This is a program to calculate a value that represents the colony/cells in an invasive growth assay.
#The program starts by enhancing the contrast in the well image, then counts the number of pixels that exceed a threshold set by the user.
#It was written by Helen Murphy in March 2024 and uses the sci-kit image package.
#The user must determine appropriate cut-off values.
#The program should be run on the pre-wash and post-wash images separately. The 96-colony images should first be processed by splitrows.py. 
#To calculate IG, divide the pixels of a post-wash colony by the pre-wash value.


#import all the necessary libraries
import skimage
import os
from skimage import io, data, filters
from skimage import util
from skimage.morphology import disk
from skimage import exposure
import math
import glob
import numpy

#Specify the location of the files, which will be in "data" if splitrows.py was run.
#In the same directory, make sure there is a directory called "processedimages".
os.chdir('path/to/input')

adherencedata= []
white_pixels= []
all_pixels= []
filenumber = 1
datasingle = []
datadouble = []
datalist = []
final_list = []

#Set parameter values for the program.

#This is for the "disk function" which is used when the original image has its contrast enhanced; it respresents the radius.  
num=15
#Set the value for the color thresholds; each user should choose their own.
#110 seems to work well for pre-wash and 120 for post-wash.
white_threshold = 110

#orders files numerically
for files in glob.glob("*"):
    if len(files) == 10:
        datasingle.append(files)
    elif len(files) == 11:
        datadouble.append(files)
        
datasingle.sort()
for data in datasingle:
    final_list.append(data)

datadouble.sort()
for data2 in datadouble:
    final_list.append(data2)

print (final_list)


for images in final_list:
    #loops through each of the images

    #gives files to skimage
    AdherenceWell  = io.imread(images)
    #x and y coordinates in the image
    i = 0
    j = 0
	#list of all the x- coordinates for the white pixels
    white_x = []
	#list of all the y- coordinates for the white pixels
    white_y = []

#uses pixel thresholds to sort as white, filamentous, or background
    for i in range(len(AdherenceWell)):
        for j in range(len(AdherenceWell[i])):
            if AdherenceWell[i][j] > white_threshold:
                AdherenceWell[i][j] = 255
                white_x.append(i)
                white_y.append(j)
       
            else:
                AdherenceWell[i][j] = 0

    skimage.io.imsave('path/to/output/'+str(filenumber)+'-processed.jpg', AdherenceWell)     
    adherence = len(white_x)
    adherencedata.append(adherence)
    print (filenumber)
    filenumber += 1

numpy.savetxt('path/to/output/invasivedata.txt', adherencedata)
