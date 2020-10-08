import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

digits, label = load_digits(return_X_y=True)
model = PCA(n_components=2)
model.fit(digits)

transformed = model.transform(digits)

plt.scatter(transformed[:, 0], transformed[:, 1], c=label, alpha=0.5,
            cmap='rainbow')

plt.xlabel('component1')
plt.ylabel('component2')
plt.colorbar()
plt.show()

check_model = PCA()
check_model.fit(digits)
plt.plot(np.cumsum(check_model.explained_variance_ratio_))
plt.xlabel('n components')
plt.ylabel('accuracy')
plt.show()
