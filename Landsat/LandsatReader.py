import numpy as np
import rasterio
import glob
import os

class LandsatReader:
    """
    LandsatReader
        Containet for multi-spectral data from Landsat-8/9.
    
    Attributes:
        datacube : 3D-Array (11, :, :)
    
    Methods:
        get_bands()

    """
    def __init__(self, dir_path):
        self.dir_path = dir_path
    
    def get_bands(self):
        bands = []
        for i in range(1, 12):
            band_files = glob.glob(os.path.join(self.dir_path, f"*B{i}.TIF"))
            if not band_files:
                continue
            with rasterio.open(band_files[0]) as src:
                b = src.read(1)
                bands.append(b)
        return bands