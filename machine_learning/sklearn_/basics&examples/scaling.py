from sklearn.preprocessing import StandardScaler
import numpy as np

random_numbers = np.random.rand(4, 2)
random_numbers *= 10

scaler = StandardScaler()
scaler.fit(random_numbers)

scaled = scaler.transform(random_numbers)

print(random_numbers)
print(scaled)

exit()
