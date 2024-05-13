import numpy as np
import os
from skimage import io
from stardist.models import StarDist3D
from csbdeep.utils import normalize
import glob
import tensorflow as tf
from utils.utils import readImage


input_path = "path/to/images"
output_path = "path/to/masks"
mask_suffix = "_mask.tif"
file_format = ".czi"
nucleus_channel = 2


image_files = glob.glob(f"{input_path}/*{file_format}")

print("available devices: ",tf.config.list_physical_devices('GPU'))

model = StarDist3D(None, name='MEC0.3', basedir='models')

def segment(img_path):

    new_image = readImage(img_path)
    
    normalized = normalize(new_image[:,:,:,nucleus_channel])

    labels, _ = model.predict_instances(normalized, n_tiles=(6,6,3))

    directory, filename = os.path.split(img_path)
    without_extension, extension = os.path.splitext(filename)
    mask_file_name = f"{without_extension}{mask_suffix}"
    mask_path = os.path.join(output_path, mask_file_name)

    io.imsave(mask_path, labels)

for image_path in image_files:
    segment(image_path)
    

