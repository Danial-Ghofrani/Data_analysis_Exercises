import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Manually input the city data


cities_data = [
    {'City': 'City1', 'Population': 9616007/30, 'Latitude': 35.6892, 'Longitude': 51.3890},
    {'City': 'City2', 'Population': 500000, 'Latitude': 24.466667, 'Longitude': 54.366669},
    {'City': 'City3', 'Population': 750000, 'Latitude': 26.4207, 'Longitude': 50.0888},
    # Add more cities as needed
]

# Initialize Basemap
lon_min, lon_max = 42, 65  # Example longitudes for the map boundaries
lat_min, lat_max = 20, 42  # Example latitudes for the map boundaries

m = Basemap(projection='merc', llcrnrlon=lon_min, llcrnrlat=lat_min, urcrnrlon=lon_max, urcrnrlat=lat_max,
            resolution='i')

# Draw coastlines, countries, and other features
m.drawcoastlines()
m.drawcountries()
m.drawmapboundary(fill_color='aqua')
m.fillcontinents(color='coral', lake_color='aqua')

# Draw parallels and meridians
m.drawparallels(range(int(lat_min), int(lat_max), 5), labels=[1, 0, 0, 0], fontsize=10)
m.drawmeridians(range(int(lon_min), int(lon_max), 5), labels=[0, 0, 0, 1], fontsize=10)

# Plot cities
for city in cities_data:
    lat = city['Latitude']
    lon = city['Longitude']
    population = city['Population']
    city_name = city['City']

    # Calculate the size of the marker based on population
    marker_size = population / 1000000 * 100  # Example scaling factor

    # Convert latitude and longitude to map coordinates
    try:
        x, y = m(lon, lat)
        print(f"Plotting {city_name} at coordinates ({lon}, {lat}) -> Map coordinates: ({x}, {y})")

        # Plot the city on the map
        m.plot(x, y, 'o', markersize=marker_size, alpha=0.5, color='red')
        plt.text(x, y, city_name, fontsize=9, ha='right', va='bottom')
    except Exception as e:
        print(f"Error plotting {city_name} at coordinates ({lon}, {lat}): {e}")

# Display the map
plt.title('Cities and Population Size')
plt.show()