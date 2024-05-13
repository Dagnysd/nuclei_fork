
# Nucleus Segmentation and Analysis

This project was created for the master thesis Automated Image Analysis for Studying Cellular Effects in the Mouse Hippocampus. It consists of two pretrained nucleus segmentation models using the Stardist alorithm, as well as functionality for measuring nuclear properties and exporting them for further analysis. Additionally, example files for model training, nucleus segmentation, and data analysis is included.


## Installation

Not all personal computers are suited to running local segmentation. This is therefore an optional addition, and it is possible to run the property measurement and data analysis components by only following the base install instructions. 


### Base install

Navigate to the desired directory and clone the project
```bash
  cd directory
  git clone https://github.com/jvgrini/nuclei.git
```
Create a virtual environment, navigate to the project directory and install dependencies
```bash
  cd nuclei
  pip install -r requirements.txt
```

### Local segmentation

Using a GPU for segmentation requires an installation of the CUDA Toolkit. Download and instructions are found at https://developer.nvidia.com/cuda-toolkit. Please see https://www.tensorflow.org/install for system specific instructions.

After installing CUDA, install Tensorflow and Stardist
```bash
  pip install tensorflow
  pip install stardist
```

## Pretrained models

The segmentation algorithm used is the Stardist algorithm. More information on this project can be in the project repository at https://github.com/stardist/stardist.

Two pretrained models for segmentation of nuclei in 3D fluorescence microscopy images of mouse brain sections are included. 

#### Note
Both models were trained on images with resolutions of approximately 0.35 x 0,35 x 0,9 along the x, y, and z, axes respectively. Resampling may be necessary for images of differing resolutions.


### Models

#### Hippocampus 1.0

Trained on images of mouse hippocampi from sections of thicknesses of 5 and 30 um.


#### MEC0.1

Trained on the same immages as Hippcoampus 1.0 in addition to images of the entorhinal cortex of mice. 
## Usage/Examples

Several example files are included in the project repository.

### Training and segmentation

Training and segmentation can be done locally as demonstrated in the example files *example_train.py* and *example_segment.py*.

For training, a path to both the training images (X), and the ground truth labels (y) must be provided. 

```python
   X = sorted(glob("X/*.tif"))
   Y = sorted(glob("y/*.tif"))
```
For information on hyperparameter selection and configuration, please consult the Stardist repository.

segmentation, the following information must be provided.

```python
   input_path = "path/to/images"
   output_path = "path/to/masks"
   mask_suffix = "_mask.tif"
   file_format = ".czi"
   nucleus_channel = 2
```

Jupyter notebooks demonstrating how to train and segment using a Google Colab runtime are also provided in the *examples_colab* folder.

The implementation has been tested on the image formates .TIFF, .czi, and .lsm. Other formats may not work as intended without modifying the *readImage()* function


### Property measurements

From a set of images and masks the properties of each nucleus can be measured by following the instructions provided in the file *example_measureDataset.py".

### Data analysis

Jupyter notebooks demonstrating some analyses of generated data are provided in the folder *dataAnalysisNotebooks*
