import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np

# Open the .nc file
file_path = 'NetCDF/PACE_OCI.20240422_20240429.L3m.8D.CARBON.V2_0.carbon_phyto.4km.NRT.nc'
dataset = nc.Dataset(file_path)

# Print the dataset to understand its structure
print(dataset)

# Extract latitude, longitude, and the variable of interest
lat = dataset.variables['lat'][:]
lon = dataset.variables['lon'][:]
variable = dataset.variables['carbon_phyto'][:]

# Plot the data
plt.figure(figsize=(10, 6))
plt.pcolormesh(lon, lat, variable, shading='auto')
plt.colorbar(label='Variable Units')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Georeferenced Image from .nc File')
plt.show()