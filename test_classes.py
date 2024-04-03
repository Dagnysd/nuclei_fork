from utils import match_images_and_masks, initializeImages, createDataframe, match_images_and_masks_without_ROI, measureNuclei
from plot_functions import plotNeuronsRegions, plotNeuronsRegionsbyRegion, plotRegionNeuronsDensity
from image import Image
import os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

contra_image_folder = 'imagesAndMasks\GFAP\images\contra'
ipsi_image_folder = "imagesAndMasks\GFAP\images\ipsi"
HI_mask_folder = 'imagesAndMasks\GFAP\masks'
roi_folder = 'imagesAndMasks\GFAP\ROI_extended'

sham_image_folder ="imagesAndMasks\GFAP\images\sham"
sham_mask_folder = "imagesAndMasks\GFAP\masks"

sham_images = match_images_and_masks(sham_image_folder, sham_mask_folder,roi_folder)
print(sham_images)
ipsi_images = match_images_and_masks(ipsi_image_folder, HI_mask_folder,roi_folder)
contra_images = match_images_and_masks(contra_image_folder, HI_mask_folder,roi_folder)
contra_objects = initializeImages(contra_images)
ipsi_objects = initializeImages(ipsi_images)
sham_objects = initializeImages(sham_images)


nucleus_df = pd.DataFrame()
image_df = pd.DataFrame()


contra_df, contraImages_df = measureNuclei(contra_objects, 'Contra')
nucleus_df = pd.concat([nucleus_df, contra_df])
image_df = pd.concat([image_df, contraImages_df])

ipsi_df, ipsiImages_df = measureNuclei(ipsi_objects, 'Ipsi')
nucleus_df = pd.concat([nucleus_df, contra_df])
image_df = pd.concat([image_df, contraImages_df])

sham_df, shamImages_df = measureNuclei(sham_objects, 'Sham')
nucleus_df = pd.concat([nucleus_df, contra_df])
image_df = pd.concat([image_df, contraImages_df])


nucleus_df = nucleus_df.dropna(axis=1, how='all')
nucleus_df.to_csv("dataAnalysisNotebooks/csv/nuclei_gfap_test.csv", index=False)
image_df.to_csv("dataAnalysisNotebooks/csv/images_gfap_test.csv", index=False)