# Satellite-Image-Analysis
by Ahmad Salehi

This repository contains optical satellite data products along with Python scripts for the analysis and processing of satellite imagery.

To download Landsat-8 data set: https://github.com/dsal/Satellite-Image-Analysis/releases/tag/Landsat_8

**Landsat 8 Optical Data Products and Spectral Bands**

Landsat 8 is a multispectral Earth observation satellite that provides high-quality optical imagery for environmental monitoring, land cover classification, vegetation analysis, and water quality assessment. The satellite captures data through the Operational Land Imager (OLI), which records surface reflectance in multiple spectral bands. Each band is designed to highlight specific features of the Earth's surface.


| Band | Name                         | Wavelength (µm) | Spatial Resolution (m) | Description                                                      |
| ---- | ---------------------------- | --------------- | ---------------------- | ---------------------------------------------------------------- |
| 0    | Ultra Blue (Coastal/Aerosol) | 0.43–0.45       | 30                     | Designed for coastal water penetration and aerosol detection.    |
| 1    | Blue                         | 0.45–0.51       | 30                     | Useful for mapping water bodies, soil/vegetation discrimination. |
| 2    | Green                        | 0.53–0.59       | 30                     | Sensitive to vegetation vigor and chlorophyll absorption.        |
| 3    | Red                          | 0.64–0.67       | 30                     | Key for vegetation discrimination and soil contrast.             |
| 4    | Near Infrared (NIR)          | 0.85–0.88       | 30                     | Highlights healthy vegetation and water bodies.                  |
| 5    | Shortwave IR (SWIR) 1        | 1.57–1.65       | 30                     | Sensitive to moisture content in soil and vegetation.            |
| 6    | Shortwave IR (SWIR) 2        | 2.11–2.29       | 30                     | Useful for detecting snow, clouds, and geology.                  |
| 7    | Cirrus                       | 1.36–1.38       | 30                     | Detects high-altitude cirrus clouds.                             |

