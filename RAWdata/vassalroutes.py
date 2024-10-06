import netCDF4 as nc
import matplotlib.pyplot as plt
import numpy as np
import geopandas as gpd
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os
from datetime import datetime, timedelta

# Path to the NetCDF folder and GeoJSON file
netcdf_folder = 'NetCDF'
vessel_routes_geojson_path = 'Shipping_Lanes_v1.geojson'

# Function to extract start date from filename and calculate end date
def extract_date_range(start_date_str):
    start_date = datetime.strptime(start_date_str, '%Y.%m.%d')
    end_date = start_date + timedelta(days=7)
    return start_date, end_date

# Load vessel routes from GeoJSON file
def load_vessel_routes(geojson_path):
    vessel_routes = gpd.read_file(geojson_path)
    return vessel_routes

# Initial start date
start_date_str = '2024.04.22'

# Load vessel routes
vessel_routes = load_vessel_routes(vessel_routes_geojson_path)
print("Vessel routes data loaded successfully.")

# Iterate over all .nc files in the NetCDF folder
for filename in sorted(os.listdir(netcdf_folder)):
    if filename.endswith('.nc'):
        print(f"Processing {filename}...")
        file_path = os.path.join(netcdf_folder, filename)
        
        # Extract start and end dates
        start_date, end_date = extract_date_range(start_date_str)
        date_range = f'{start_date.strftime("%Y.%m.%d")} - {end_date.strftime("%Y.%m.%d")}'
        
        # Open the .nc file
        dataset = nc.Dataset(file_path)
        
        # Extract latitude, longitude, and the variable of interest
        lat = dataset.variables['lat'][:]
        lon = dataset.variables['lon'][:]
        variable = dataset.variables['carbon_phyto'][:]
        
        # Create a figure with a cartopy projection
        fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={'projection': ccrs.PlateCarree()})
        
        # Plot the NetCDF data
        mesh = ax.pcolormesh(lon, lat, variable, shading='auto', transform=ccrs.PlateCarree(), cmap='viridis')
        plt.colorbar(mesh, ax=ax, orientation='vertical', label='Carbon Phyto Units')
        
        ax.coastlines()
        ax.add_feature(cfeature.BORDERS, linestyle=':')
        ax.gridlines(draw_labels=True)
        
        # Plot the vessel routes
        vessel_routes.plot(ax=ax, edgecolor='red', linewidth=1, transform=ccrs.PlateCarree())
        
        # Set title to include vessel routes
        title_with_routes = f'Plankton Aerosol Cloud data between {date_range} with Vessel Routes'
        plt.title(title_with_routes)
        
        # Save the figure as a PNG image (with vessel routes)
        output_file_path_with_routes = f'Plankton_Aerosol_Cloud_data_between_{date_range}_with_Vessel_Routes.png'
        plt.savefig(output_file_path_with_routes, bbox_inches='tight')
        print(f"Map saved to {output_file_path_with_routes}")
        
        # Close the plot to free memory
        plt.close(fig)
        
        # Update the start date for the next iteration
        start_date_str = end_date.strftime('%Y.%m.%d')