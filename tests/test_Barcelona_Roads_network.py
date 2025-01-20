# tests/test_Barcelona_Roads_network.py
import pytest
from CityInsight.Barcelona_Roads_networks import plot_barcelona_roads_network


def test_plot_barcelona_roads_network():
    # Run the plot function with show_plot=False during testing (skip displaying)
    plot_barcelona_roads_network(show_plot=False)

    # Check if the plot file exists after the function runs
    import os
    assert os.path.exists('barcelona_roads_parks_libraries_museums.png')
