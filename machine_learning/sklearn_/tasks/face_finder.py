from itertools import chain
from sys import exit

import matplotlib.pyplot as plt
import numpy as np
from skimage import color, data, feature, transform
from sklearn.datasets import fetch_lfw_people
from sklearn.feature_extraction.image import PatchExtractor
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC


def extract_hog():
    """Example function - original picture and HOG picture in one slide"""

    chelsea = data.chelsea()
    image = color.rgb2gray(chelsea)
    hog_vec, hog_vis = feature.hog(image, visualize=True)

    fig, ax = plt.subplots(1, 2, figsize=(12, 6), subplot_kw={'xticks': [], 'yticks': []})

    ax[0].imshow(image)
    ax[0].set_title('original')

    ax[1].imshow(hog_vis)
    ax[1].set_title('hog')

    plt.show()


def extract_patches(image, quantity, patch_size, scale=1.0):
    extracted_patch_size = tuple((float(scale) * np.array(patch_size)).astype(int))
    extractor = PatchExtractor(extracted_patch_size, quantity, random_state=0)
    patches = extractor.transform(image[np.newaxis])

    if scale != 1:
        patches = np.array([transform.resize(patch, patch_size) for patch in patches])

    return patches


def searching_frame(img, patch_size, axis_step=2, ordinate_step=2, scale=1.0):
    n_i, n_j = (int(scale * s) for s in patch_size)

    for i in range(0, img.shape[0] - n_i, axis_step):
        for j in range(0, img.shape[1] - n_j, ordinate_step):
            patch = img[i:i + n_i, j:j + n_j]

            if float(scale) != 1.0:
                patch = transform.resize(patch, scale)

            yield (i, j), patch


def main():
    faces = fetch_lfw_people()
    positive_patches = faces.images

    topics = ['camera', 'coins', 'text', 'page', 'clock', 'moon', 'coffee']
    images = [color.rgb2gray(getattr(data, name)()) for name in topics]

    negative_patches = np.vstack([extract_patches(im, 1000, positive_patches[0].shape, scale)
                                  for im in images for scale in [0.5, 1.0, 2.0]])

    x_train = np.array([feature.hog(im) for im in chain(positive_patches, negative_patches)])
    y_train = np.zeros(x_train.shape[0])
    y_train[:positive_patches.shape[0]] = 1

    svc_grid_score = GridSearchCV(LinearSVC(), n_jobs=3, param_grid={'C': [0.5, 1.0, 2.5, 4.0, 5.5]})
    svc_grid_score.fit(x_train, y_train)
    print(f'Best grid score = {svc_grid_score.best_score_}')

    model = svc_grid_score.best_estimator_
    model.fit(x_train, y_train)

    test_image = data.astronaut()
    test_image = color.rgb2gray(test_image)
    test_image = transform.rescale(test_image, 0.5)

    plt.imshow(test_image, cmap='gray')
    plt.axis('off')
    plt.show()

    indices, patches = zip(*searching_frame(test_image, positive_patches[0].shape))
    patches_hog = np.array([feature.hog(patch) for patch in patches])

    labels = model.predict(patches_hog)

    fig, ax = plt.subplots()
    ax.imshow(test_image, cmap='gray')
    ax.axis('off')

    n_i, n_j = positive_patches[0].shape
    indices = np.array(indices)

    for i, j in indices[labels == 1]:
        ax.add_patch(plt.Rectangle((j, i), n_j, n_i, edgecolor='red', alpha=0.2, facecolor='none'))

    plt.show()


if __name__ == '__main__':
    main()
    exit()
