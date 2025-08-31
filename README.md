# Satellite-Image-Analysis

by Ahmad Salehi

This repository contains optical satellite data products along with Python scripts for the analysis and processing of satellite imagery.

Landsat is the longest continuously operating Earth observation satellite program. The first Landsat satellite was launched in 1972, and the most recent, Landsat 9, was launched in 2021. Landsat missions continue—Landsat Next is in development and will support current spectral bands associated with Landsat 8 and 9, as well as 15 additional bands (26 bands in total; Figure 12.1). Landsat Next is anticipated to launch in 2030.

<img width="792" height="612" alt="image1-5" src="https://github.com/user-attachments/assets/04f5dd0e-c339-4d08-b007-86c166bda915" />


***Landsat 9 Optical Data Products and Spectral Bands***

Landsat 9 is a multispectral Earth observation satellite that provides high-quality optical imagery for environmental monitoring, land cover classification, vegetation analysis, and water quality assessment. The satellite captures data through the Operational Land Imager 2 (OLI-2) and the Thermal Infrared Sensor 2 (TIRS-2). Each spectral band is designed to highlight specific features of the Earth's surface, from vegetation and water bodies to thermal properties.

To download Landsat-9 dataset: https://github.com/dsal/Satellite-Image-Analysis/releases/tag/Landsat_9
Please read the discription of the uploaded release!

***Landsat 9 OLI-2 & TIRS-2 Spectral Bands***

| Band | Name                         | Wavelength (µm) | Spatial Resolution (m) | Description                                                      |
| ---- | ---------------------------- | --------------- | ---------------------- | ---------------------------------------------------------------- |
| 1    | Ultra Blue (Coastal/Aerosol) | 0.43–0.45       | 30                     | Designed for coastal water penetration and aerosol detection.    |
| 2    | Blue                         | 0.45–0.51       | 30                     | Useful for mapping water bodies, soil/vegetation discrimination. |
| 3    | Green                        | 0.53–0.59       | 30                     | Sensitive to vegetation vigor and chlorophyll absorption.        |
| 4    | Red                          | 0.64–0.67       | 30                     | Key for vegetation discrimination and soil contrast.             |
| 5    | Near Infrared (NIR)          | 0.85–0.88       | 30                     | Highlights healthy vegetation and water bodies.                  |
| 6    | Shortwave IR (SWIR) 1        | 1.57–1.65       | 30                     | Sensitive to moisture content in soil and vegetation.            |
| 7    | Shortwave IR (SWIR) 2        | 2.11–2.29       | 30                     | Useful for detecting snow, clouds, and geology.                  |
| 8    | Panchromatic                 | 0.50–0.68       | 15                     | Provides high-resolution grayscale imagery.                      |
| 9    | Cirrus                       | 1.36–1.38       | 30                     | Detects high-altitude cirrus clouds.                             |
| 10   | TIRS 1                       | 10.60–11.19     | 100                    | Thermal infrared band for surface temperature.                   |
| 11   | TIRS 2                       | 11.50–12.51     | 100                    | Thermal infrared band for surface temperature.                   |

Landsat 9 essentially continues the Landsat 8 mission, but with OLI-2 and TIRS-2 instruments for improved radiometric stability.

All bands except the thermal (TIRS) and panchromatic bands have 30 m resolution.

The panchromatic band is 15 m, and thermal bands are 100 m (resampled to 30 m for most products).
