from skimage import io, measure
import czifile
import glob
import os
import pandas as pd
import numpy as np


from nucleus import Nucleus

def getNucleiFromImage(imageFilename, maskFilename, imageName):

    if '.czi' in imageFilename:
        image = czifile.imread(imageFilename)
        image = np.squeeze(image)
        image = np.transpose(image, (1,2,3,0))
    else:
        image = io.imread(imageFilename)
    labels = io.imread(maskFilename)
    properties = measure.regionprops(labels, intensity_image=image)
    
    nuclei = []

    for prop in properties:
        region_label = prop.label
        region_area = prop.area
        centroid = prop.centroid
        region_mean_intensity = prop.mean_intensity
        if len(region_mean_intensity) > 3:
            ch1_intensity, ch2_intensity, ch3_intensity, ch4_intensity= region_mean_intensity
        elif len(region_mean_intensity) == 3:
            ch1_intensity, ch2_intensity, ch3_intensity= region_mean_intensity
            ch4_intensity = None
        else:
            ch1_intensity, ch2_intensity= region_mean_intensity
            ch3_intensity = None
            ch4_intensity = None
        nuclei.append(
            Nucleus(imageName,
                    region_label,
                    region_area,
                    centroid,
                    ch1_intensity,
                    ch2_intensity,
                    ch3_intensity,
                    ch4_intensity,
            ))

    return nuclei
def match_images_and_masks(image_folder, mask_folder, roi_folder=None, imageFormat='.czi', maskSuffix='_mask.tif', roiSuffix='_roi.tif'):
    image_files = []
    images = glob.glob(os.path.join(image_folder, f'*{imageFormat}'))
    for image_path in images:
        mask_path = os.path.join(mask_folder, os.path.basename(image_path).replace(imageFormat, maskSuffix))
        if roi_folder != None:
            roi_path = os.path.join(roi_folder, os.path.basename(image_path).replace(imageFormat, roiSuffix))
        if os.path.exists(mask_path) and os.path.exists(roi_path):
            image_files.append([image_path, mask_path, roi_path])
        else:
            image_files.append([image_path, mask_path])
    return image_files


def initializeImages(images, useROI, scale):
    from image import Image
    objects = []
    for image_info in images:
        name = os.path.basename(image_info[0])
        if len(image_info) > 2:  
            image_obj = Image(name, image_info[0], image_info[1], image_info[2], scale=scale)
            objects.append(image_obj)
        elif useROI==False:
            image_obj = Image(name, image_info[0], image_info[1],scale=scale)
            objects.append(image_obj)
        else:
            print(f"No ROI found for image {name}")
    return objects

def createDataframe(obj, condition):

    nuclei_data = []

    for nucleus in obj.nuclei:
        nucleus_dict = {
                'Condition': condition,
                'ImageName': nucleus.imageName,
                'Label': nucleus.label,
                'Area': nucleus.area,
                'Centroid': nucleus.centroid,
                'CellType': nucleus.cellType,
                'Location': nucleus.location,
                'Ch1Intensity': nucleus.ch1Intensity,
                'Ch2Intensity': nucleus.ch2Intensity,
                'Ch3Intensity': nucleus.ch3Intensity,
                'Ch4Intensity': nucleus.ch4Intensity,
                'gfpPositive': nucleus.gfpPositive,
                'CytoCh1Intensity': nucleus.cyto_ch1_intensity,
                'CytoCh2Intensity': nucleus.cyto_ch2_intensity,
                'CytoCh3Intensity': nucleus.cyto_ch3_intensity,
                'CytoCh4Intensity': nucleus.cyto_ch4_intensity,
                # Add more attributes as needed
        }
            # Append the nucleus dictionary to the nuclei_data list
        nuclei_data.append(nucleus_dict)

# Create a DataFrame from the list of dictionaries
    nuclei_df = pd.DataFrame(nuclei_data)
    return nuclei_df


def createImageDataframe(object, condition):
    image_dict = {
        'Condition': condition,
        'ImageName': [object.name],
        'CA1Volume': [object.ca1Volume],
        'CA3Volume': [object.ca3Volume],
        'DGVolume': [object.dgVolume],
        'Ch1Intensity': [object.ch1Intensity],
        'Ch2Intensity': [object.ch2Intensity],
        'Ch3Intensity': [object.ch3Intensity],
        'Ch4Intensity': [object.ch4Intensity],
        'Shape': [object.image.shape],
        'Ch1Background': [object.ch1Background],
        'Ch2Background': [object.ch2Background],
        'Ch3Background': [object.ch3Background],
        'Ch4Background': [object.ch4Background],
    }
    image_df = pd.DataFrame(image_dict)
    return image_df

def readImage(imagePath):
    import czifile
    if 'czi' in imagePath:
        image = czifile.imread(imagePath)
        image = np.squeeze(image)
        image = np.transpose(image, (1,2,3,0))
    else:
        image = io.imread(imagePath)
    return image

def measureNuclei(objects, condition, roiNames, measureCyto = False, useROI = False):
    nucleus_df = pd.DataFrame()
    images_df = pd.DataFrame()
    for object in objects:
        print(object.name, len(object.nuclei))
        #object.nuclei = object.classifyCells(inspect_classified_masks=False, plot_selectionChannel=False)
        object.calculateIntensitiesImage()
        object.measureBackground()
        if useROI:
            object.calculate_nuclei_locations(roiNames)
            object.calculateRoiVolume()
        if measureCyto:
            object.measureCyto()
        #object.visualize_nuclei_locations()
        object_df = createDataframe(object, condition=condition)
        image_df = createImageDataframe(object, condition)
        nucleus_df = pd.concat([nucleus_df, object_df], ignore_index=True)
        images_df = pd.concat([images_df, image_df], ignore_index=True)
    
    return nucleus_df, images_df

def measureDataset(conditions, imageFolders, maskFolder, roiFolder, imageFormat, maskSuffix, roiSuffix, nucleusDataframeOutputPath, imageDataframeOutputPath, roiNames, useROI=False, measureCyto=False, scale=[1,1,1]):
    nucleus_df = pd.DataFrame()
    image_df = pd.DataFrame()

    for index, condition in enumerate(conditions):
        imageFolder = imageFolders[index]
        images = match_images_and_masks(imageFolder, maskFolder, roiFolder, imageFormat=imageFormat, maskSuffix=maskSuffix, roiSuffix=roiSuffix)
        objects = initializeImages(images, useROI)
        n_df, i_df = measureNuclei(objects, condition, useROI=useROI, measureCyto=measureCyto, roiNames=roiNames)
        nucleus_df = pd.concat([nucleus_df, n_df])
        image_df = pd.concat([image_df, i_df])

    nucleus_df = nucleus_df.dropna(axis=1, how='all')
    nucleus_df.to_csv(nucleusDataframeOutputPath, index=False)
    image_df.to_csv(imageDataframeOutputPath, index=False)
        

