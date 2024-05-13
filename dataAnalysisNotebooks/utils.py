

def readImage(imagePath):
    import czifile
    from skimage import io
    import numpy as np
    if 'czi' in imagePath:
        image = czifile.imread(imagePath)
        image = np.squeeze(image)
        image = np.transpose(image, (1,2,3,0))
    else:
        image = io.imread(imagePath)
    return image