# Data Notes

## Karu LGA Boundary

- Source: GRID3 Nigeria Geospatial Data
- Website: https://grid3.org/geospatial-data-nigeria
- Dataset: Nigeria administrative boundaries
- Study area: Karu Local Government Area, Nasarawa State
- Geometry: Polygon
- Purpose: Defines the boundary of the study area and provides the spatial extent for extracting and analysing other datasets.
- Coverage: The layer covers the Karu LGA study area.

## Settlement Locations

- Source: GRID3 Nigeria Geospatial Data
- Website: https://grid3.org/geospatial-data-nigeria
- Dataset: Nigeria settlement locations
- Study area: Karu LGA, Nasarawa State
- Geometry: Point
- Purpose: Shows the distribution of settlements within and around the study area and will be used for comparison with waste disposal locations.
- Coverage: Settlement locations are distributed across the study area, although the completeness of mapped settlements depends on the source dataset.

## Waste Disposal Sites

- Source: Baseline Survey and Field Observation of Waste Management in Karu LGA, Nasarawa State, Nigeria
- Source platform: ResearchGate
- Dataset type: Waste observation/dumpsite locations
- Number of observations: 98
- Geometry: Point
- Purpose: Represents observed waste disposal locations and serves as the main dataset for the project.
- Coverage: The dataset contains 98 observed waste disposal locations across Karu LGA.
- Data quality note: The locations represent observed sites and should not automatically be interpreted as every waste disposal site existing in Karu LGA.

## OpenStreetMap Features

- Source: OpenStreetMap
- Website: https://www.openstreetmap.org/
- Extraction method: QuickOSM
- Study area: Karu LGA
- Geometry: Depends on the OSM feature queried
- Purpose: Provides supporting geographic information such as roads, waterways and other mapped features.
- Coverage: OpenStreetMap coverage is not uniform. Some areas contain more mapped features than others, particularly in built-up areas.
- Data quality note: Missing OSM features do not necessarily mean that the feature does not exist on the ground. They may indicate that it has not been mapped.

## Digital Elevation Model

- Source: OpenTopography / Copernicus DEM
- Website: https://portal.opentopography.org/raster?opentopoID=OTSDEM.032021.4326.3
- Dataset type: Digital Elevation Model
- Geometry: Raster
- Purpose: Provides elevation information for the study area and can be used to derive terrain characteristics such as slope.
- Coverage: The DEM covers the study area.
- Data quality note: The raster contains elevation values for individual cells. Areas with no valid elevation value are represented by the dataset's NoData value.

## Data Inspection

The datasets were opened and inspected in QGIS.

The following properties were checked:

- Number of features/rows
- Attribute field names
- Field data types
- Presence of null values
- Geometry type
- Spatial coverage
- Relationship between attribute-table records and map features

The attribute tables were connected to the map using QGIS selection tools. Selecting a record in the attribute table highlighted the corresponding feature on the map, and selecting a feature on the map highlighted its corresponding record.

## Coverage and Limitations

The Karu LGA boundary provides the main spatial extent of the project.

The waste disposal dataset contains 98 observed locations and provides the main point dataset for the project.

GRID3 settlement data provides supporting information about the distribution of settlements.

OpenStreetMap data provides useful supporting features, but its coverage depends on the extent to which features have been mapped by OpenStreetMap contributors. Therefore, unmapped roads, waterways or other features should not automatically be interpreted as absent on the ground.

These limitations will be considered during later spatial analysis.

## Data Management

Raw downloaded datasets are stored in:

```text
data/raw/
