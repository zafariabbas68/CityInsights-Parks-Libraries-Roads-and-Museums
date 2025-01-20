from setuptools import setup, find_packages

setup(
    name="CityInsight",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "osmnx",
        "geopandas",
        "matplotlib"
    ],
    description="A Python package to visualize parks, libraries, roads, and museums in various cities.",
    long_description="CityInsight provides tools to plot and analyze various city features like parks, libraries, roads, and museums using OpenStreetMap data.",
    long_description_content_type="text/plain",
    author="Your Name",
    author_email="your.email@example.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
