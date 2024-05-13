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


conditions = ['HI_Sham','Sham_Contra', 'Contra', 'Ipsi']
imageFolders = ["imagesAndMasks/tunel/sham", 'imagesAndMasks/tunel/contra', "imagesAndMasks/tunel/ipsi"] 
maskFolder = "imagesAndMasks/tunel/masks"
roiFolder = 'imagesAndMasks/tunel/roi_extended'
scale = [0.9278, 0.3459, 0.3459]
useROI = True
roiNames = {1: 'CA1', 2: 'CA3', 3: 'DG'}
measureCyto = False

imageFormat = '.czi'
maskSuffix = '_mask.tif'
roiSuffix = '_roi.tif'

nucleusDataframeOutputPath = 'dataAnalysisNotebooks/csv/nuclei_tunnel_test.csv'
imageDataframeOutputPath = 'dataAnalysisNotebooks/csv/images_tunnel_test.csv'



measureDataset(conditions, imageFolders, maskFolder, roiFolder, imageFormat, maskSuffix, roiSuffix, nucleusDataframeOutputPath, imageDataframeOutputPath, useROI=useROI, measureCyto=measureCyto, roiNames = roiNames, scale = scale)

