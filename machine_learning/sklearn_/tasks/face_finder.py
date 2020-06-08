from sys import exit

import matplotlib.pyplot as plt
from skimage import color, data, feature, transform
from sklearn.datasets import fetch_lfw_people

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


def extract_patches(image, N, scale):
    pass


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
