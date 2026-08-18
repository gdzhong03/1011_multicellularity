#This is a program to calculate a value that represents the adherence to a well in a plastic adherence assay.
#The program starts by enhancing the contrast in the well image, then counts the number of pixels that exceed a threshold set by the user.
#It was written by Helen Murphy in March 2024 and uses the sci-kit image package.
#The user must determine appropriate cut-off values.
#To calculate percent adherence, divide the adherence pixels by the area of the well in pixels.
#Measure this by determining the diameter of the well in pixels and calculating the area. It will be the same value for all wells.

#REMEMBER TO FLIP THE IMAGE IF NECESSARY TO GET A1 IN THE UPPER LEFTHAND CORNER


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

#Specify the directory with the images to be processed.
#In the same directory, make sure there is a directory called "processedimages".
os.chdir('/Users/helldawg/Helen/Work/Projects/Predation-Multicellularity-Armaan/ImageAnalysis/data')

adherencedata= []
white_pixels= []
all_pixels= []
filenumber = 1
datasingle = []
datadouble = []
datalist = []
final_list = []

#Set the value for the color thresholds; each user should choose their own.
white_threshold = 40

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
    AdherenceWell   = io.imread(images)
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

    skimage.io.imsave('/Users/helldawg/Helen/Work/Projects/Predation-Multicellularity-Armaan/ImageAnalysis/processedimages/'+str(filenumber)+'-processed.jpg', AdherenceWell)     
    adherence = len(white_x)
    adherencedata.append(adherence)
    print (filenumber)
    filenumber += 1

numpy.savetxt('/Users/helldawg/Helen/Work/Projects/Predation-Multicellularity-Armaan/ImageAnalysis/adherencedata.txt', adherencedata)
