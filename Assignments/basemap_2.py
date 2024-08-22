import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

csv_file = "Cities_data.CSV"
cities_data = pd.read_csv(csv_file)



lon_min, lon_max = 42, 65
lat_min, lat_max = 20, 42
m = Basemap(projection='merc', llcrnrlon=lon_min, llcrnrlat=lat_min, urcrnrlon=lon_max, urcrnrlat=lat_max,
            resolution='i')
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='white')
m.fillcontinents(color='gray', lake_color='white')
m.drawparallels(range(int(lat_min), int(lat_max) + 1, 5), labels=[1, 0, 0, 0], fontsize=10)
m.drawmeridians(range(int(lon_min), int(lon_max) + 1, 5), labels=[0, 0, 0, 1], fontsize=10)



for index, row in cities_data.iterrows():
    lat = row['Latitude']
    lon = row['Longitude']
    population = row['Population']
    city_name = row['City']
    marker_size = population /2000
    x, y = m(lon, lat)
    m.scatter(x,y, s=marker_size, alpha=0.3, color="red")
    plt.text(x, y, city_name, fontsize=9, ha='right', va='bottom')



plt.title('Cities and Population Size')
plt.show()
