# Month 1 Summary - Spatial Analysis

## Project Overview

This month marked the beginning of my GIS project under **GeoDev Lab Africa, Cohort One**.

The project focuses on using geospatial data and spatial analysis to investigate the relationship between waste disposal sites and surrounding settlements within **Karu, Aso-Kodupe and Bagaji-Agada wards of Karu Local Government Area, Nasarawa State, Nigeria**.

The project is being developed around the following research question:

> **Which settlements within Karu, Aso-Kodupe and Bagaji-Agada wards of Karu Local Government Area, Nasarawa State, are potentially exposed to environmental risks associated with waste disposal sites?**

Month 1 focused mainly on understanding the problem, identifying and preparing the required datasets, carrying out data quality checks, and performing the first spatial analysis using buffer operations.

---

# Week 1 - Defining the Problem and Initial Data Collection

## Project Question

The initial project question was:

> **Which communities in Karu Local Government Area, Nasarawa State, are potentially exposed to environmental risks associated with waste disposal sites?**

As the project developed, the scope was refined from the entire Karu LGA to three selected wards:

- Karu
- Aso-Kodupe
- Bagaji-Agada

The unit of analysis was also refined from "communities" to "settlements" to better match the available spatial data.

## Initial Data Requirements

I identified several datasets that could support the project, including:

- Waste disposal site locations
- Administrative and ward boundaries
- Settlement locations
- Population data
- Rivers and waterways
- Digital Elevation Model (DEM)
- Slope
- Land use/land cover
- Rainfall
- Geological data
- Soil data

## Data Sources

Some of the main data sources identified for the project include:

| Dataset | Source |
|---|---|
| Waste disposal sites | Karu Waste Management Baseline Survey / Field Data |
| Administrative boundaries | GRID3 |
| Settlement data | GRID3 |
| Population data | WorldPop |
| Rivers and waterways | OpenStreetMap |
| Digital Elevation Model | OpenTopography / Copernicus GLO-30 |
| Land use/land cover | ESA WorldCover |
| Rainfall | CHIRPS |
| Geological data | Nigeria Geological Survey Agency (NGSA) |
| Soil data | ISRIC / SoilGrids |

## Week 1 Focus

The main focus during Week 1 was understanding the project problem and identifying the spatial datasets required to answer the research question.

I also began working with waste disposal point locations and exploring how they relate spatially to surrounding areas and settlements.

### What I Learned

Week 1 helped me understand that a good GIS project begins with a clearly defined question and appropriate datasets.

I also learned that the availability, format, spatial coverage and quality of datasets can strongly influence the type of analysis that can be carried out.

---

# Week 2 - Data Exploration and GIS Processing

## Data Exploration

During Week 2, I continued working with the identified datasets and explored their spatial characteristics in QGIS.

The main objective was to understand the structure of the datasets and determine how they could be prepared for the project.

I examined:

- Spatial reference systems
- Layer geometry
- Attribute tables
- Spatial extent
- Dataset formats
- Relevant fields
- Compatibility between different datasets

## Initial GIS Processing

The datasets were brought into QGIS for visualization and processing.

I began organizing the project data into appropriate categories and examining how the different spatial layers could eventually be combined.

The waste disposal points were treated as the main locations from which proximity analysis would later be performed.

## Project Organization

I also began organizing the project files so that raw source data could be kept separate from processed datasets.

This approach was important because it allowed the original source files to remain unchanged while processed versions could be used for analysis.

### What I Learned

Week 2 showed me the importance of understanding the structure of spatial data before beginning analysis.

I also learned that GIS analysis is not only about creating maps. Data organization, coordinate systems, attribute information and data quality all affect the reliability of the final analysis.

---

# Week 3 - Data Preparation, Reprojection and Quality Checks

## Study Area

The study area was refined to:

- Karu Ward
- Aso-Kodupe Ward
- Bagaji-Agada Ward

within Karu Local Government Area, Nasarawa State, Nigeria.

The selected ward boundaries were used to define the area of interest and prepare the datasets for spatial analysis.

## Coordinate Reference System

The source datasets were primarily provided in:

**EPSG:4326 - WGS 84**

For spatial analysis, the data were reprojected to:

**EPSG:32632 - WGS 84 / UTM Zone 32N**

EPSG:32632 was selected because the study area falls within UTM Zone 32N and the projected coordinate system provides metre-based units suitable for distance and area calculations.

This was particularly important because the next stage of the project involved buffer analysis using distances measured in metres.

## Data Reprojection and Clipping

The relevant datasets were reprojected from EPSG:4326 to EPSG:32632.

The datasets were then clipped to the selected study area.

The processed layers were checked after reprojection and clipping to ensure that they were correctly aligned and suitable for further analysis.

Raw source files were kept unchanged in:

`data/raw/`

Processed datasets were stored in:

`data/processed/`

## Quality Checks

Five main quality checks were carried out.

### 1. CRS Check

**Result:** Source layers were in EPSG:4326 and the prepared layers were reprojected to EPSG:32632.

**Decision:** EPSG:32632 was retained as the working CRS for spatial analysis.

### 2. Geometry Check

**Result:** The processed layers were checked for invalid or problematic geometries after clipping and reprojection.

**Decision:** The prepared layers were retained for analysis after the geometry check.

### 3. Study Area / Clipping Check

**Result:** The datasets were clipped to the selected ward study area.

**Decision:** The clipped datasets were retained as the analysis versions.

### 4. Attribute Check

**Result:** Attribute tables were reviewed to confirm that relevant fields were retained after processing and that the datasets could support the planned analysis.

**Decision:** The required attributes were retained and the processed layers were used for analysis.

### 5. Output / Analysis-Ready Check

**Result:** The processed datasets were saved as an analysis-ready GeoPackage and checked in QGIS to confirm that the layers could be loaded and used.

**Decision:** The GeoPackage was retained as the final analysis-ready dataset.

## Area Check

Area calculations were checked after reprojection using square metres and square kilometres to confirm that measurements were being made correctly in the projected CRS.

## File Organization

The project data were organized as follows:

```text
data/
├── raw/
└── processed/
    └── karu_week3.gpkg

The raw files were left untouched, while the processed datasets were stored separately for analysis.

## What I Learned

Week 3 helped me understand why coordinate reference systems are important in spatial analysis.

I learned that geographic coordinates such as latitude and longitude are not always appropriate for distance-based operations. Reprojecting the data into a suitable projected CRS made it possible to perform measurements and buffer analysis using metres.

# Week 4 - Buffer Analysis and Spatial Relationship

## Spatial Operation

For Week 4, I used a buffer operation to investigate the area surrounding identified waste disposal points.

I selected the buffer operation because the project question involves understanding the relationship between settlements and their distance from waste disposal locations.

A buffer creates a defined area around each waste point, allowing nearby settlements and other spatial features to be identified based on a specified distance.

The analysis was carried out using the projected:

**EPSG:32632 - WGS 84 / UTM Zone 32N**

prepared during Week 3.

This was necessary because the buffer distances were measured in metres.

## Buffer Distances

The analysis considered different proximity ranges around the waste disposal points:

- 0-250 m
- 250-500 m
- 500 m-1 km
- 1-2 km
- Greater than 2 km

These distance ranges are being used as proximity zones to support the assessment of potential environmental exposure.

They do not, by themselves, confirm contamination or establish a health risk.

## Expected Result

I expected the buffer operation to create defined zones around each waste disposal point.

I expected the resulting buffer areas to show which parts of the surrounding study area fall within selected distances from the waste locations.

I also expected the output to contain the same number of waste-point features as the input where the buffers were created without dissolving overlapping features.

## What I Got

The buffer operation successfully produced buffer geometries around the waste points using distances measured in metres.

The resulting layer can be used to compare waste disposal locations with surrounding settlement data and identify settlements that fall within the selected proximity zones.

The analysis result was checked by:

- Viewing the buffer output on the map
- Inspecting the attribute table
- Checking individual buffer features against their corresponding waste points

## Preliminary Settlement Results

After applying the proximity analysis to the settlement data, the following settlement counts were observed within the selected buffer distances:

| Buffer distance | Settlement count |
|---|---:|
| 250 m | 1,674 |
| 500 m | 4,868 |
| 1 km | 16,098 |
| 2 km | 52,853 |

These figures represent settlements identified within the selected proximity zones.

The results should be interpreted as potential exposure based on spatial proximity, rather than confirmed contamination or direct health risk.

## What Surprised Me

One challenge during the analysis was that some supporting settlement data required for the final interpretation and map production was not initially available in the exact form needed.

This showed me that a spatial operation can be completed successfully while the interpretation of the result still depends on having the appropriate supporting datasets.

It also reinforced the importance of data availability and quality in GIS analysis.

## Data Still Needed

The main supporting dataset required for the next stage is an appropriate settlement/populated-place dataset covering the selected wards.

This will allow me to:

- Overlay settlements on the waste disposal buffers
- Identify settlements within each proximity zone
- Compare settlement locations with waste disposal sites
- Examine the spatial distribution of potentially exposed settlements
- Support the development of the final exposure map

Additional datasets such as population, rivers, elevation, land use/land cover, rainfall, geology and soil may also be incorporated to provide additional environmental context.

# Month 1 Key Outputs

During the first month, I moved from defining the project problem to carrying out my first spatial analysis.

The main outputs from Month 1 include:

- A refined GIS research question
- Identification of the three selected study wards
- Identification of the required spatial datasets
- Initial waste disposal point mapping
- Data organization into raw and processed datasets
- Reprojection of datasets from EPSG:4326 to EPSG:32632
- Clipping of datasets to the selected study area
- Geometry and attribute quality checks
- Creation of an analysis-ready GeoPackage
- Buffer analysis around waste disposal points
- Preliminary settlement proximity counts
- Initial spatial interpretation of potential exposure zones

# What I Learned During Month 1

Month 1 helped me understand that GIS analysis is a process that begins long before the final map is produced.

Some of the key lessons I gained include:

- A clear research question guides the entire GIS workflow.
- The quality and availability of spatial data affect the type and reliability of analysis that can be performed.
- Coordinate reference systems are important for accurate distance and area calculations.
- Data preparation is an essential part of spatial analysis, not just a preliminary step.
- Quality checks help ensure that datasets are suitable for analysis.
- Buffer analysis can be used to investigate spatial relationships based on distance.
- Proximity to a waste disposal site indicates potential exposure, but does not by itself confirm contamination or health risk.
- Different datasets need to be combined to provide a stronger environmental interpretation.

# Month 1 Reflection

At the beginning of the month, the project was mainly an idea based on a question about waste disposal sites and surrounding settlements.

By the end of Month 1, I had developed a structured GIS workflow involving data collection, data preparation, coordinate transformation, quality checks and spatial analysis.

The buffer analysis provided the first spatial relationship needed for the project. It allowed me to move from simply mapping waste disposal points to investigating how their locations relate to nearby settlements.

The preliminary results also showed me that spatial analysis is an iterative process. The availability of additional datasets will allow the analysis to become more detailed as the project progresses.
