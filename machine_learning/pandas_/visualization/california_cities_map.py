import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.basemap import Basemap

cities = pd.read_csv('../../../california_cities.csv')

lat = cities['latd'].values
lon = cities['longd'].values
population = cities['population_total'].values
area = cities['area_total_km2'].values

figure = plt.figure(figsize=(8, 8))
california_map = Basemap(projection='lcc', resolution='h', lat_0=37.5, lon_0=-119, width=1E6, height=1.2E6)
california_map.shadedrelief()
california_map.drawcoastlines(color='blue')
california_map.drawcountries(color='red')
california_map.drawstates(color='yellow')

california_map.scatter(lon, lat, latlon=True, c=np.log10(population), s=area, alpha=0.5)

plt.colorbar(label=r'$\log_{10}({\rm population})$')
plt.clim(3, 7)

for label_area in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.5, s=label_area, label=str(label_area) + r' km$^2$')

plt.legend(scatterpoints=1, loc='lower left')
plt.show()
