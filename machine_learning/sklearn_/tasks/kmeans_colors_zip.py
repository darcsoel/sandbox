from sys import exit

import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans
from sklearn.datasets import load_sample_image

original_image = load_sample_image('china.jpg')

plt.imshow(original_image)
plt.show()

image = original_image / 255.0
image = image.reshape(image.shape[0] * image.shape[1], image.shape[2])

model = MiniBatchKMeans(n_clusters=16)
model.fit(image)

recolored = model.cluster_centers_[model.predict(image)]

new_image = recolored.reshape(original_image.shape)
plt.imshow(new_image)
plt.show()

exit()
