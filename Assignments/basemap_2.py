import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd

csv_file = "Cities_data.CSV"

cities_data = pd.read_csv(csv_file)

# Ensure the latitude and longitude are numeric
cities_data['Latitude'] = pd.to_numeric(cities_data['Latitude'], errors='coerce')
cities_data['Longitude'] = pd.to_numeric(cities_data['Longitude'], errors='coerce')

# Drop rows with invalid lat/lon values
cities_data = cities_data.dropna(subset=['Latitude', 'Longitude'])

lon_min, lon_max = 42, 65
lat_min, lat_max = 20, 42

m = Basemap(projection='merc', llcrnrlon=lon_min, llcrnrlat=lat_min, urcrnrlon=lon_max, urcrnrlat=lat_max,
            resolution='i')

# Draw coastlines, countries, and other features
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral', lake_color='aqua')


m.drawparallels(range(int(lat_min), int(lat_max) + 1, 5), labels=[1, 0, 0, 0], fontsize=10)
m.drawmeridians(range(int(lon_min), int(lon_max) + 1, 5), labels=[0, 0, 0, 1], fontsize=10)


for index, row in cities_data.iterrows():
    lat = row['Latitude']
    lon = row['Longitude']
    population = row['Population']
    city_name = row['City']

    # Calculate the size of the marker based on population
    marker_size = population /200000 # Example scaling factor

    # Convert latitude and longitude to map coordinates
    try:
        x, y = m(lon, lat)
        print(f"Plotting {city_name} at coordinates ({lon}, {lat}) -> Map coordinates: ({x}, {y})")

        # Plot the city on the map
        m.plot(x, y, 'o', markersize=marker_size, alpha=0.5, color='red')
        plt.text(x, y, city_name, fontsize=9, ha='right', va='bottom')
    except Exception as e:
        print(f"Error plotting {city_name} at coordinates ({lon}, {lat}): {e}")


plt.title('Cities and Population Size')
plt.show()