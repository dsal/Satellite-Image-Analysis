# Satellite-Image-Analysis
by Ahmad Salehi

This repository contains optical satellite data products along with Python scripts for the analysis and processing of satellite imagery.


**Landsat 8 Optical Data Products and Spectral Bands**

Landsat 8 is a multispectral Earth observation satellite that provides high-quality optical imagery for environmental monitoring, land cover classification, vegetation analysis, and water quality assessment. The satellite captures data through the Operational Land Imager (OLI), which records surface reflectance in multiple spectral bands. Each band is designed to highlight specific features of the Earth's surface.

**To download Landsat-8 data set:** https://github.com/dsal/Satellite-Image-Analysis/releases/tag/Landsat_8

Landsat 8's Operational Land Imager (OLI) provides the following spectral bands:

| Band | Name                         | Wavelength (µm) | Spatial Resolution (m) | Description                                                      |                                                                    |
| ---- | ---------------------------- | --------------- | ---------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------ |
| 1    | Ultra Blue (Coastal/Aerosol) | 0.43–0.45       | 30                     | Designed for coastal water penetration and aerosol detection.    |                                                                    |
| 2    | Blue                         | 0.45–0.51       | 30                     | Useful for mapping water bodies, soil/vegetation discrimination. |                                                                    |
| 3    | Green                        | 0.53–0.59       | 30                     | Sensitive to vegetation vigor and chlorophyll absorption.        |                                                                    |
| 4    | Red                          | 0.64–0.67       | 30                     | Key for vegetation discrimination and soil contrast.             |                                                                    |
| 5    | Near Infrared (NIR)          | 0.85–0.88       | 30                     | Highlights healthy vegetation and water bodies.                  |                                                                    |
| 6    | Shortwave IR (SWIR) 1        | 1.57–1.65       | 30                     | Sensitive to moisture content in soil and vegetation.            |                                                                    |
| 7    | Shortwave IR (SWIR) 2        | 2.11–2.29       | 30                     | Useful for detecting snow, clouds, and geology.                  |                                                                    |
| 8    | Panchromatic                 | 0.50–0.68       | 15                     | Provides high-resolution grayscale imagery.                      |                                                                    |
| 9    | Cirrus                       | 1.36–1.38       | 30                     | Detects high-altitude cirrus clouds.                             |                                                                    |
| 10   | TIRS 1                       | 10.60–11.19     | 100                    | Thermal infrared band for surface temperature.                   |                                                                    |
| 11   | TIRS 2                       | 11.50–12.51     | 100                    | Thermal infrared band for surface temperature.                   |
