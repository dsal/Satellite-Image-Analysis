# Satellite-Image-Analysis

by Ahmad Salehi

# Landsat 8/9

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
<sub>
| Attribute         | Band 1 | Band 2 | Band 3 | Band 4 | Band 5 | Band 6 | Band 7 | Band 8 | Band 9 | Band 10 | Band 11 | Band 12 | Band 13 | Band 14 | Band 15 | Band 16 | Band 17 | Band 18 | Band 19 | Band 20 | Band 21 | Band 22 | Band 23 |
|-------------------|--------|--------|--------|--------|--------|--------|--------|--------|--------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| **Wavelength (nm)** | 503 | 510 | 519 | 535 | 549 | 570 | 584 | 600 | 614 | 635 | 649 | 660 | 669 | 679 | 690 | 699 | 711 | 722 | 734 | 750 | 764 | 782 | 799 |
| **FWHM (nm)**      | 20.1 | 20.4 | 20.8 | 21.4 | 22.0 | 22.8 | 23.4 | 24.0 | 24.6 | 25.4 | 26.0 | 26.4 | 26.8 | 27.2 | 27.6 | 28.0 | 28.4 | 28.9 | 29.4 | 30.0 | 30.6 | 31.3 | 32.0 |
| **Notes**          | Blue-green region | Blue-green region | Green region | Green region | Green region | Yellow region | Yellow region | Orange region | Orange region | Red region | Red region | Red region | Red region | Red region | Red region | Red region | Red-edge region | Red-edge region | Red-edge region | NIR region | NIR region | NIR region | NIR region |
</sub>

# Sentinel-2

| Band        | B1                 | B2   | B3    | B4   | B5         | B6         | B7         | B8                 | B8A        | B9           | B10   | B11     | B12     |
|------------|------------------|------|-------|------|------------|------------|------------|------------------|------------|-------------|-------|---------|---------|
| **Name**   | Coastal/Aerosol   | Blue | Green | Red  | Red Edge 1 | Red Edge 2 | Red Edge 3 | Near Infrared (NIR) | Narrow NIR | Water Vapour | Cirrus | SWIR 1  | SWIR 2  |
| **Wavelength (µm)** | 0.433–0.453      | 0.450–0.510 | 0.530–0.590 | 0.640–0.680 | 0.705–0.745 | 0.740–0.780 | 0.775–0.815 | 0.785–0.900      | 0.855–0.875 | 0.935–0.955 | 1.360–1.390 | 1.580–1.640 | 2.010–2.090 |
| **Resolution (m)**  | 60               | 10   | 10    | 10   | 20         | 20         | 20         | 10               | 20         | 60           | 60    | 20      | 20      |
| **Description** | Designed for coastal water penetration and aerosol detection. | Useful for mapping water bodies, soil/vegetation discrimination. | Sensitive to vegetation vigor and chlorophyll absorption. | Key for vegetation discrimination and soil contrast. | Useful for vegetation classification and monitoring. | Sensitive to vegetation stress and chlorophyll content. | Enhances vegetation monitoring and biomass estimation. | Highlights healthy vegetation and water bodies. | Provides additional info for vegetation analysis. | Useful for atmospheric water vapor estimation. | Detects high-altitude cirrus clouds. | Sensitive to moisture content in soil and vegetation. | Useful for detecting snow, clouds, and geology. |
