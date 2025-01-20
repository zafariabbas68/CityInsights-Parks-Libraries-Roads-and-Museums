import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_boston_roads_network(show_plot=True):
    # Define the place and feature types
    place_name = "Boston, Massachusetts, USA"

    # Get the boundary of Boston as a polygon
    boston_polygon = ox.geocode_to_gdf(place_name).geometry.iloc[0]

    # Get parks data from OSM using the polygon
    parks = ox.features_from_polygon(boston_polygon, tags={'leisure': 'park'})

    # Get libraries data from OSM using the polygon
    libraries = ox.features_from_polygon(boston_polygon, tags={'amenity': 'library'})

    # Get road network data from OSM
    roads = ox.graph.graph_from_polygon(boston_polygon, network_type='all')
    roads_gdf = ox.graph_to_gdfs(roads, nodes=False, edges=True)

    # Filter roads to include a broader set of categories
    major_roads = roads_gdf[roads_gdf['highway'].isin([
        'primary', 'secondary', 'tertiary', 'motorway', 'motorway_link',
        'residential', 'unclassified', 'trunk', 'primary_link', 'secondary_link', 'tertiary_link'
    ])]

    # Create the plot with higher DPI for better resolution
    fig, ax = plt.subplots(figsize=(12, 12), dpi=300)

    # Plot the filtered major road network in dark grey (closer to black)
    major_roads.plot(ax=ax, color='#404040', linewidth=0.8, label='Major Roads')

    # Plot parks in dark green with alpha for transparency
    parks.plot(ax=ax, color='#004c4c', alpha=0.8)

    # Plot libraries in orange with adjusted markersize
    libraries.plot(ax=ax, color='#f25f0c', markersize=30)

    # Create custom legend handles
    park_patch = mpatches.Patch(color='#004c4c', label='Parks')
    library_patch = mpatches.Patch(color='#f25f0c', label='Libraries')
    road_patch = mpatches.Patch(color='#404040', label='Major Roads')

    # Add the custom legend
    ax.legend(handles=[road_patch, park_patch, library_patch], loc='upper left')

    # Set the title with larger font size
    ax.set_title("City of Boston\nParks, Libraries, and Major Roads", fontsize=20, weight='bold', loc='left')

    # Remove axes for a clean look
    ax.set_axis_off()

    # Save the plot as PNG
    plt.savefig('boston_roads_parks_libraries.png', dpi=300, bbox_inches='tight')

    # Show the plot if not running the test
    if show_plot:
        plt.show()
    else:
        plt.close()  # Close the plot to avoid keeping it open during tests

