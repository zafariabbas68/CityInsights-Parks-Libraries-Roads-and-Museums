# tests/test_Amsterdam_Roads_network.py
import pytest
from CityInsight.Amsterdam_Roads_networks import plot_amsterdam_roads_network


def test_plot_amsterdam_roads_network():
    # Run the plot function with show_plot=False during testing (skip displaying)
    plot_amsterdam_roads_network(show_plot=False)

    # Check if the plot file exists after the function runs
    import os
    assert os.path.exists('amsterdam_roads_parks_libraries_museums.png')
