from sys import exit

import matplotlib.pyplot as plt
from skimage import color, data, feature, transform
from sklearn.datasets import fetch_lfw_people
import numpy as np
from sklearn.feature_extraction.image import PatchExtractor


def extract_hog():
    chelsea = data.chelsea()
    image = color.rgb2gray(chelsea)
    hog_vec, hog_vis = feature.hog(image, visualize=True)

    fig, ax = plt.subplots(1, 2, figsize=(12, 6), subplot_kw={'xticks': [], 'yticks': []})

    ax[0].imshow(image)
    ax[0].set_title('original')

    ax[1].imshow(hog_vis)
    ax[1].set_title('hog')

    plt.show()


def extract_patches(image, quantity, patch_size, scale=1):
    extracted_patch_size = tuple((float(scale) * np.array(patch_size)).astype(int))
    extractor = PatchExtractor(extracted_patch_size, quantity, random_state=0)
    patches = extractor.transform(image[np.newaxis])

    if scale != 1:
        patches = np.array([transform.resize(patch, patch_size) for patch in patches])

    return patches


def main():
    faces = fetch_lfw_people()
    positive_faces = faces.images

    negative_topics = ['camera', 'coins', 'text', 'page', 'clock', 'moon', 'coffee']
    negative_images = color.rgb2gray(getattr(data, name)() for name in negative_topics)

    pass


if __name__ == '__main__':
    extract_hog()
    main()
    exit()
