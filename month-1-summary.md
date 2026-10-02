# Month 1 Summary - Spatial Analysis

## Project Question

**Which settlements within Karu, Aso-Kodupe and Bagaji-Agada wards of Karu Local Government Area, Nasarawa State, are potentially exposed to environmental risks associated with waste disposal sites?**

## Week 1 - Project Definition and Data Collection

I began the project by defining the research problem and identifying the spatial datasets needed to investigate the relationship between waste disposal sites and surrounding settlements.

The main datasets identified included:

- Waste disposal site locations
- Ward boundaries
- Settlement data
- Population data
- Rivers and waterways
- Digital Elevation Model (DEM)
- Land use/land cover
- Rainfall
- Geological data
- Soil data

This stage helped establish the data requirements and overall direction of the project.

## Week 2 - Data Exploration and Processing

During Week 2, I explored the available datasets in QGIS and examined their spatial extent, coordinate reference systems, geometry and attribute information.

I also began organizing the project files and preparing the datasets for further analysis.

This stage showed me the importance of understanding and organizing spatial data before carrying out GIS analysis.

## Week 3 - Data Preparation and Quality Checks

During Week 3, I prepared the datasets for spatial analysis.

The source datasets were primarily in **EPSG:4326 (WGS 84)** and were reprojected to **EPSG:32632 (WGS 84 / UTM Zone 32N)**.

The datasets were clipped to the selected study area covering **Karu, Aso-Kodupe and Bagaji-Agada wards**.

I also carried out:

- CRS checks
- Geometry checks
- Study area and clipping checks
- Attribute checks
- Analysis-ready output checks

The processed datasets were saved separately from the raw files, with the final analysis-ready data stored in a GeoPackage.

This stage helped me understand why an appropriate projected CRS is important for accurate distance and area calculations.

## Week 4 - Buffer Analysis

During Week 4, I moved from data preparation to spatial analysis by applying a **buffer operation** around the identified waste disposal points.

The analysis used distances measured in metres within EPSG:32632.

The proximity zones considered were:

- 0-250 m
- 250-500 m
- 500 m-1 km
- 1-2 km
- Greater than 2 km

The buffer output was checked by viewing the map, inspecting the attribute table and comparing individual buffers with their corresponding waste points.

### Preliminary Results

The settlement proximity analysis produced the following counts:

| Buffer distance | Settlement count |
|---|---:|
| 250 m | 1,674 |
| 500 m | 4,868 |
| 1 km | 16,098 |
| 2 km | 52,853 |

These results represent potential exposure based on spatial proximity. They do not confirm contamination or establish a direct health risk.

## Key Lessons from Month 1

Month 1 helped me understand that GIS analysis involves more than producing maps. The process includes:

- Defining a clear research question
- Identifying appropriate datasets
- Preparing and checking spatial data
- Selecting a suitable coordinate reference system
- Performing spatial analysis
- Interpreting results carefully

I also learned that the availability and quality of supporting datasets can affect how far a spatial analysis can be interpreted.

## Month 1 Reflection

Over the four weeks, I moved from defining a GIS research problem to preparing spatial data and performing my first proximity analysis.

The buffer analysis provided the first spatial relationship needed for the project by showing areas surrounding waste disposal points based on distance.

The next stage will involve combining the buffer results with settlement and other environmental datasets to better understand areas of potential environmental exposure.

**Programme:** GeoDev Lab Africa, Cohort One  
**Study Area:** Karu, Aso-Kodupe and Bagaji-Agada Wards, Karu LGA, Nasarawa State, Nigeria
