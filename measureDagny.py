from utils import match_images_and_masks, initializeImages, createDataframe, match_images_and_masks_without_ROI, measureNuclei
from image import Image
import os
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


image_folder_dg = 'imagesAndMasks/liv/dg'
image_folder_ca1 = 'imagesAndMasks/liv/ca1'
image_folder_ca3 = 'imagesAndMasks/liv/ca3'
image_folder_mec = 'imagesAndMasks/liv/mec'
mask_folder = 'imagesAndMasks/liv/masks'


image_files_dg = match_images_and_masks_without_ROI(image_folder_dg, mask_folder)
image_files_ca1 = match_images_and_masks_without_ROI(image_folder_ca1, mask_folder)
image_files_ca3 = match_images_and_masks_without_ROI(image_folder_ca3, mask_folder)
image_files_mec = match_images_and_masks_without_ROI(image_folder_mec, mask_folder)

image_objects_dg = initializeImages(image_files_dg)
image_objects_ca1 = initializeImages(image_files_ca1)
image_objects_ca3 = initializeImages(image_files_ca3)
image_objects_mec = initializeImages(image_files_mec)



nucleus_df = pd.DataFrame()
image_df = pd.DataFrame()

dg_df, contraImages_df = measureNuclei(image_objects_dg, 'DG', useROI=False)
nucleus_df = pd.concat([nucleus_df, dg_df])
image_df = pd.concat([image_df, contraImages_df])

ca1_df, ipsiImages_df = measureNuclei(image_objects_ca1, 'CA1', useROI=False)
nucleus_df = pd.concat([nucleus_df, ca1_df])
image_df = pd.concat([image_df, contraImages_df])

ca3_df, shamImages_df = measureNuclei(image_objects_ca3, 'CA3', useROI=False)
nucleus_df = pd.concat([nucleus_df, ca3_df])
image_df = pd.concat([image_df, contraImages_df])

mec_df, shamImages_df = measureNuclei(image_objects_mec, 'MEC', useROI=False)
nucleus_df = pd.concat([nucleus_df, mec_df])
image_df = pd.concat([image_df, contraImages_df])


nucleus_df = nucleus_df.dropna(axis=1, how='all')
nucleus_df.to_csv("dataAnalysisNotebooks/csv/nuclei_liv_test.csv", index=False)
image_df.to_csv("dataAnalysisNotebooks/csv/images_liv_test.csv", index=False)

