# CityInsight/Barcelona_Roads_networks.py
import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_barcelona_roads_network(show_plot=True):
    # Define the place and feature types
    place_name = "Barcelona, Spain"

    # Get the boundary of Barcelona as a polygon
    barcelona_polygon = ox.geocode_to_gdf(place_name).geometry.iloc[0]

    # Get parks data from OSM using the polygon
    parks = ox.features_from_polygon(barcelona_polygon, tags={'leisure': 'park'})

    # Get libraries data from OSM using the polygon
    libraries = ox.features_from_polygon(barcelona_polygon, tags={'amenity': 'library'})

    # Get museums data from OSM using the polygon
    museums = ox.features_from_polygon(barcelona_polygon, tags={'tourism': 'museum'})

    # Get road network data from OSM
    roads = ox.graph.graph_from_polygon(barcelona_polygon, network_type='all')
    roads_gdf = ox.graph_to_gdfs(roads, nodes=False, edges=True)

    # Filter roads to include a broader set of categories
    major_roads = roads_gdf[roads_gdf['highway'].isin([
        'primary', 'secondary', 'tertiary', 'motorway', 'motorway_link',
        'residential', 'unclassified', 'trunk', 'primary_link', 'secondary_link', 'tertiary_link'
    ])]

    # Create the plot with higher DPI for better resolution
    fig, ax = plt.subplots(figsize=(12, 12), dpi=300)

    # Plot the filtered major road network in a lighter black (dark grey)
    major_roads.plot(ax=ax, color='#333333', linewidth=0.8, label='Major Roads')

    # Plot parks in dark green with alpha for transparency
    parks.plot(ax=ax, color='#004c4c', alpha=0.8)

    # Plot libraries in orange with adjusted markersize
    libraries.plot(ax=ax, color='#f25f0c', markersize=30)

    # Plot museums in dark blue with adjusted markersize
    museums.plot(ax=ax, color='#1f77b4', markersize=50, label="Museums")

    # Create custom legend handles
    park_patch = mpatches.Patch(color='#004c4c', label='Parks')
    library_patch = mpatches.Patch(color='#f25f0c', label='Libraries')
    road_patch = mpatches.Patch(color='#333333', label='Major Roads')
    museum_patch = mpatches.Patch(color='#1f77b4', label='Museums')

    # Add the custom legend
    ax.legend(handles=[road_patch, park_patch, library_patch, museum_patch], loc='upper left')

    # Set the title with larger font size
    ax.set_title("City of Barcelona\nParks, Libraries, Museums, and Roads", fontsize=20, weight='bold', loc='left')

    # Remove axes for a clean look
    ax.set_axis_off()

    # Save the plot as PNG with a white background
    plt.savefig('barcelona_roads_parks_libraries_museums.png', dpi=300, bbox_inches='tight', facecolor='white', edgecolor='white')

    # Show the plot only if not in test mode
    if show_plot:
        plt.show()
    else:
        plt.close()  # Close the plot to avoid displaying during tests
