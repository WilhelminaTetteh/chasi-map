import pandas as pd
import folium

# Load the data from the CSV file
file_path = 'Tonys Communities - Sheet1.csv'  # Make sure the file name matches exactly
data = pd.read_csv(file_path)

# Display the dataframe to ensure it's loaded correctly
print(data)

# Create a map centered at the average location of all communities
avg_lat = data['Latitude'].mean()
avg_lon = data['Longitude'].mean()
community_map = folium.Map(location=[avg_lat, avg_lon], zoom_start=10)

# Add markers for each community
for index, row in data.iterrows():
    folium.Marker(location=[row['Latitude'], row['Longitude']], popup=row['Community']).add_to(community_map)

# Save the map to an HTML file
community_map.save('community_map.html')
