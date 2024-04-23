import numpy as np
import os
from skimage import io
from stardist.models import StarDist3D
from csbdeep.utils import normalize
import glob
import tensorflow as tf
from utils import readImage


spacing = ([0.3459, 0.3459, 0.9278])

folder_path = "imagesAndMasks/test_compare"
image_files = glob.glob(f"{folder_path}/*.tif")

print("available devices: ",tf.config.list_physical_devices('GPU'))

model = StarDist3D(None, name='MEC0.3', basedir='models')

def segment(img_path):

    new_image = readImage(img_path)
    
    if new_image.shape[-1] == 4:
        normalized = normalize(new_image[:,:,:,3])
    else:
        normalized = normalize(new_image)

    labels, _ = model.predict_instances(normalized, n_tiles=(6,6,3))

    directory, filename = os.path.split(img_path)
    without_extension, extension = os.path.splitext(filename)
    mask_file_name = f"{without_extension}_mask.tif"
    mask_path = os.path.join("imagesAndMasks/test_compare", mask_file_name)

    io.imsave(mask_path, labels)

for image_path in image_files:
    segment(image_path)
    

