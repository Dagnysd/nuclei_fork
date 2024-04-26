import numpy as np
import os
from skimage import io, filters, measure, morphology, exposure, segmentation, feature
from scipy.ndimage import distance_transform_edt, label
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import make_scorer, jaccard_score
from sklearn.base import BaseEstimator, TransformerMixin
import sys
sys.path.insert(1, 'D:/Users\Jonas/nuclei')
from utils import readImage

sigma = 2.5
kernel_size = 7
clip_limit = 0.1
kernel_thresh = 251
opening_radius = 5
closing_radius = 1
footprint = 13
footprint_z = 9
min_region_size = 500

img_path = "D:/Users\Jonas/nuclei\imagesAndMasks/test_compare/test3.tif"
img = readImage(img_path)



def transform(img):
        filtered = filters.gaussian(img, sigma=sigma)
        equalized_channel = exposure.equalize_adapthist(filtered, kernel_size=kernel_size, clip_limit=clip_limit)

        # binary_volume = (equalized_channel > filters.threshold_local(equalized_channel, block_size=kernel_thresh, method='gaussian', offset=0))
        binary_volume = (equalized_channel > filters.threshold_otsu(equalized_channel))
        binary_volume = morphology.binary_opening(binary_volume, morphology.ball(radius=opening_radius))            
        binary_volume = morphology.binary_closing(binary_volume, morphology.ball(radius=closing_radius))

        labeled_volume = measure.label(binary_volume)

        filtered_labeled_volume = morphology.remove_small_objects(labeled_volume, min_size=min_region_size)
        distance = distance_transform_edt(filtered_labeled_volume, sampling=(1,1,2.6823))            
        coords = feature.peak_local_max(distance, footprint=np.ones([footprint, footprint, footprint_z]), labels=filtered_labeled_volume)
        mask = np.zeros(distance.shape, dtype=bool)
        mask[tuple(coords.T)] = True
        markers, _ = label(mask)
        labels = segmentation.watershed(-distance, markers, mask=filtered_labeled_volume)

        labels = morphology.remove_small_objects(labels, min_size=min_region_size)

        return labels

labels = transform(img)

io.imsave("archived_scripts/watershed_segment3.tif", labels)
