# Satellite-Image-Analysis

by Ahmad Salehi

This repository contains optical satellite data products along with Python scripts for the analysis and processing of satellite imagery.

# Landsat
Landsat is the longest continuously operating Earth observation satellite program. The first Landsat satellite was launched in 1972, and the most recent, Landsat 9, was launched in 2021. Landsat missions continue—Landsat Next is in development and will support current spectral bands associated with Landsat 8 and 9, as well as 15 additional bands (26 bands in total; Figure 12.1). Landsat Next is anticipated to launch in 2030.

<img width="792" height="612" alt="image1-5" src="https://github.com/user-attachments/assets/04f5dd0e-c339-4d08-b007-86c166bda915" />


***Landsat 9 Optical Data Products and Spectral Bands***

Landsat 9 is a multispectral Earth observation satellite that provides high-quality optical imagery for environmental monitoring, land cover classification, vegetation analysis, and water quality assessment. The satellite captures data through the Operational Land Imager 2 (OLI-2) and the Thermal Infrared Sensor 2 (TIRS-2). Each spectral band is designed to highlight specific features of the Earth's surface, from vegetation and water bodies to thermal properties.

To download Landsat-9 dataset: https://github.com/dsal/Satellite-Image-Analysis/releases/tag/Landsat_9

Please read the discription of the uploaded release!

***Landsat 9 OLI-2 & TIRS-2 Spectral Bands***
<sub>
| Attribute                  | Band 1 | Band 2 | Band 3 | Band 4 | Band 5 | Band 6 | Band 7 | Band 8 | Band 9 | Band 10 | Band 11 |
|-----------------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|---------|---------|
| **Name**                    | Ultra Blue (Coastal/Aerosol) | Blue | Green | Red | Near Infrared (NIR) | Shortwave IR (SWIR) 1 | Shortwave IR (SWIR) 2 | Panchromatic | Cirrus | TIRS 1 | TIRS 2 |
| **Wavelength (µm)**         | 0.43–0.45 | 0.45–0.51 | 0.53–0.59 | 0.64–0.67 | 0.85–0.88 | 1.57–1.65 | 2.11–2.29 | 0.50–0.68 | 1.36–1.38 | 10.60–11.19 | 11.50–12.51 |
| **Spatial Resolution (m)**  | 30 | 30 | 30 | 30 | 30 | 30 | 30 | 15 | 30 | 100 | 100 |
| **Description**             | Designed for coastal water penetration and aerosol detection. | Useful for mapping water bodies, soil/vegetation discrimination. | Sensitive to vegetation vigor and chlorophyll absorption. | Key for vegetation discrimination and soil contrast. | Highlights healthy vegetation and water bodies. | Sensitive to moisture content in soil and vegetation. | Useful for detecting snow, clouds, and geology. | Provides high-resolution grayscale imagery. | Detects high-altitude cirrus clouds. | Thermal infrared band for surface temperature. | Thermal infrared band for surface temperature. |
</sub>

Landsat 9 essentially continues the Landsat 8 mission, but with OLI-2 and TIRS-2 instruments for improved radiometric stability.

All bands except the thermal (TIRS) and panchromatic bands have 30 m resolution.

The panchromatic band is 15 m, and thermal bands are 100 m (resampled to 30 m for most products).

# Wyvern
Dragonette-1 is Wyvern's hyperspectral imaging satellite providing 23 spectral bands across the 503-799 nm wavelength range. It offers 5.3m resolution at nadir with a 20km swath width, ideal for precision agriculture, environmental monitoring, and resource management applications.

***Wyvern Dragonette Hyperspectral Bands***

| Band | Wavelength (nm) | FWHM (nm) | Notes             |
| ---- | ---------------------- | --------- | ----------------- |
| 1    | 503                    | 20.1      | Blue-green region |
| 2    | 510                    | 20.4      | Blue-green region |
| 3    | 519                    | 20.8      | Green region      |
| 4    | 535                    | 21.4      | Green region      |
| 5    | 549                    | 22.0      | Green region      |
| 6    | 570                    | 22.8      | Yellow region     |
| 7    | 584                    | 23.4      | Yellow region     |
| 8    | 600                    | 24.0      | Orange region     |
| 9    | 614                    | 24.6      | Orange region     |
| 10   | 635                    | 25.4      | Red region        |
| 11   | 649                    | 26.0      | Red region        |
| 12   | 660                    | 26.4      | Red region        |
| 13   | 669                    | 26.8      | Red region        |
| 14   | 679                    | 27.2      | Red region        |
| 15   | 690                    | 27.6      | Red region        |
| 16   | 699                    | 28.0      | Red region        |
| 17   | 711                    | 28.4      | Red-edge region   |
| 18   | 722                    | 28.9      | Red-edge region   |
| 19   | 734                    | 29.4      | Red-edge region   |
| 20   | 750                    | 30.0      | NIR region        |
| 21   | 764                    | 30.6      | NIR region        |
| 22   | 782                    | 31.3      | NIR region        |
| 23   | 799                    | 32.0      | NIR region        |
