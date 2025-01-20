import pytest
from CityInsight.Boston_Roads_networks import plot_boston_roads_network

def test_plot_boston_roads_network():
    # Run the plot function with show_plot=False during testing
    plot_boston_roads_network(show_plot=False)
    # You can assert something related to the plot (like checking file creation) if needed
    # For example, assert that the plot file exists after running the function
    import os
    assert os.path.exists('boston_roads_parks_libraries.png')
