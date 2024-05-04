from utils import measureDataset


#
#   This example file demonstrates how one may measure the properties of a dataset 
#


#
#   conditions
#       The identifier that distinguishes one set of images from another
#   imageFolder
#       Path to images. Position in list must correspond to position in 'conditions'
#   maskFolder
#       Path to masks
#   roiFolder
#       Path to ROI masks. This is not necesarry to analysis unless you want to distinguish between regions in the images
#
conditions = ['Sham', 'Contra', 'Ipsi']
imageFolders = ["imagesAndMasks/iba1/sham", 'imagesAndMasks/iba1/contra', "imagesAndMasks/iba1/ipsi"] 
maskFolder = "imagesAndMasks/iba1/masks"
roiFolder = 'imagesAndMasks/iba1/roi_extended'

useROI = True
measureCyto = False

imageFormat = '.lsm'
maskSuffix = '_mask.tif'
roiSuffix = '_roi.tif'

nucleusDataframeOutputPath = 'dataAnalysisNotebooks/csv/nuclei_iba1_test.csv'
imageDataframeOutputPath = 'dataAnalysisNotebooks/csv/images_iba1_test.csv'

measureDataset(conditions, imageFolders, maskFolder, roiFolder, imageFormat, maskSuffix, roiSuffix, nucleusDataframeOutputPath, imageDataframeOutputPath, useROI=useROI, measureCyto=measureCyto)

