"""
This files originate from the "New-Empty-Python-Project-Base" template:
    https://github.com/Neuraxio/New-Empty-Python-Project-Base 
Created by Guillaume Chevalier at Neuraxio:
    https://github.com/Neuraxio 
    https://github.com/guillaume-chevalier 
License: CC0-1.0 (Public Domain)
"""
from numpy import loadtxt
from tifffile import imread
from pathlib import Path


def load_data(dataset: str):
    data_dir = Path(__file__).parent / "datasets" / dataset
    sample = imread(data_dir / "sample.tif")
    psf = imread(data_dir / "psf.tif")
    initial_positions = loadtxt(data_dir / "initial_positions.csv", delimiter=",")

    return sample, psf, initial_positions
