from utils import match_images_and_masks
from plot_functions import plotNeuronsRegions
from image import Image
import os
import numpy as np
from matplotlib import pyplot as plt

image_folder = 'images_HI_contra'
mask_folder = 'masks_HI'
roi_folder = 'brain_region_masks_extended'

# sham_image_folder ="images_sham"
# sham_mask_folder = "masks_sham"

# sham_images = match_images_and_masks(sham_image_folder, sham_mask_folder, roi_folder)

images = match_images_and_masks(image_folder, mask_folder, roi_folder)
print(len(images))
image_objects = []
for image_info in images:
    name = os.path.basename(image_info[0])  
    image_obj = Image(name, image_info[0], image_info[1], image_info[2])
    image_objects.append(image_obj)
# for image_info in sham_images:
#     name = os.path.basename(image_info[0])  
#     image_obj = Image(name, image_info[0], image_info[1], image_info[2])
#     image_objects.append(image_obj)

cluster_values = []
mean_background = []
mean_signal = []
for object in image_objects:
    print(object.name, len(object.nuclei))
    mean_signal.append(object.getMeanFluorescenceChannel(channel=3))
    object.clusterMasks = object.classifyCells(inspect_classified_masks=False, plot_selectionChannel=False)
    object.clusterNuclei = object.measureClusterNucleiInImage(object.clusterMasks)
    object.ca1Clusters = object.measureClusterNucleiInRegion(object.roi, region=1, inspect_regions=False)
    object.dgClusters = object.measureClusterNucleiInRegion(object.roi, region =2, inspect_regions=False)
    object.ca3Clusters = object.measureClusterNucleiInRegion(object.roi, region=3)
    print(len(object.dgClusters[0]), len(object.dgClusters[1]), len(object.dgClusters[2]))
    #background = object.measureBackground()
    #mean_background.append(background)
    print('Non neurons: ',len(object.clusterNuclei[0]))
    print('Immature neurons: ',len(object.clusterNuclei[1]))
    print('Mature neurons: ',len(object.clusterNuclei[2]))
    fluo0, fluo1, fluo2 = object.getMeanFluorescenceChannel(3, clusters=True)
    print(np.mean(fluo0), np.mean(fluo1), np.mean(fluo2))


plotNeuronsRegions(image_objects, title="HI contralateral")