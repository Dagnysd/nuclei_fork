import napari
from skimage import io
import czifile
import numpy as np
import tifffile
from utils.utils import readImage

spacing = ([0.9278349, 0.3459441, 0.3459441])

img = readImage('imagesAndMasks/tunel/ipsi/HI 1 Ipsilateral Mouse 8 Slide 23  TUNEL assay.czi')
#mask = io.imread("imagesAndMasks/tunel/masks/Sham 1 Contralateral slide 22 TUNEL Assay_mask.tif")
#roi = io.imread("imagesAndMasks/region_masks_extended\HI 1 Contralateral Mouse 8 Slide18 G4green NeuNpink CD86red 40x 4x4 technical replica 2_mask_region.tif")
print(img.shape)
print(type(img))


viewer = napari.view_image(
    img,
    channel_axis=3,
    scale = spacing,
    ndisplay=2
)
#viewer.add_labels(mask, scale=spacing)
#viewer.add_labels(mask_star,name="star", scale=spacing)
napari.run()
