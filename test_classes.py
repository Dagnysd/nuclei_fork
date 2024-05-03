from utils import measureDataset

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

# sham_images = match_images_and_masks(sham_image_folder, sham_mask_folder,roi_folder)
# ipsi_images = match_images_and_masks(ipsi_image_folder, HI_mask_folder,roi_folder)
# contra_images = match_images_and_masks(contra_image_folder, HI_mask_folder,roi_folder)
# contra_objects = initializeImages(contra_images)
# ipsi_objects = initializeImages(ipsi_images)
# sham_objects = initializeImages(sham_images)


# nucleus_df = pd.DataFrame()
# image_df = pd.DataFrame()


# contra_df, contraImages_df = measureNuclei(contra_objects, 'Contra', useROI=True, measureCyto=True)
# nucleus_df = pd.concat([nucleus_df, contra_df])
# image_df = pd.concat([image_df, contraImages_df])

# ipsi_df, ipsiImages_df = measureNuclei(ipsi_objects, 'Ipsi', useROI=True, measureCyto=True)
# nucleus_df = pd.concat([nucleus_df, ipsi_df])
# image_df = pd.concat([image_df, ipsiImages_df])

# sham_df, shamImages_df = measureNuclei(sham_objects, 'Sham', useROI=True, measureCyto=True)
# nucleus_df = pd.concat([nucleus_df, sham_df])
# image_df = pd.concat([image_df, shamImages_df])


# nucleus_df = nucleus_df.dropna(axis=1, how='all')
# nucleus_df.to_csv("dataAnalysisNotebooks/csv/nuclei_iba1.csv", index=False)
# image_df.to_csv("dataAnalysisNotebooks/csv/images_iba1.csv", index=False)