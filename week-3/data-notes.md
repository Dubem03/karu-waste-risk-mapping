Week 3 Data Preparation and Quality Checks

CRS and preparation

Study Area

- Study area: Karu LGA, Nasarawa State, Nigeria.
- The relevant administrative boundary was used to define the study area and clip the datasets.

Coordinate Reference System

- Source CRS: EPSG:4326 (WGS 84).
- Working CRS: EPSG:32632 (WGS 84 / UTM Zone 32N).
- EPSG:32632 was selected because Karu LGA falls within UTM Zone 32N and the projected CRS provides metre-based units suitable for distance and area calculations.

Data Reprojection and Clipping

- Source datasets were reprojected from EPSG:4326 to EPSG:32632.
- The datasets were clipped to the Karu LGA study boundary.
- The processed layers were checked after reprojection and clipping.
- Raw source files were kept unchanged in "data/raw/".
- Processed files were saved in "data/processed/".

Five Quality Checks

1. CRS Check

Result: Source layers were in EPSG:4326 and the prepared layers were reprojected to EPSG:32632.

Decision: EPSG:32632 was retained as the working CRS for spatial analysis.

2. Geometry Check

Result: The processed layers were checked for invalid or problematic geometries after clipping and reprojection.

Decision: The prepared layers were retained for analysis after the geometry check.

3. Study Area / Clipping Check

Result: The datasets were clipped to the Karu LGA boundary, ensuring that the prepared data represented the study area.

Decision: The clipped datasets were retained as the analysis versions.

4. Attribute Check

Result: The attribute tables were reviewed to confirm that the relevant fields were retained after processing and that the datasets could support the planned analysis.

Decision: The required attributes were retained and the processed layers were used for analysis.

5. Output / Analysis-Ready Check

Result: The processed datasets were saved as an analysis-ready GeoPackage and checked in QGIS to confirm that the layers could be loaded and used.

Decision: The GeoPackage was retained as the final analysis-ready dataset.

Area Check

Area calculations were checked after reprojection using square metres and square kilometres to ensure that measurements were being made in the projected CRS.

File Organization

- Raw data: "data/raw/"
- Processed data: "data/processed/"
- Analysis-ready GeoPackage: "data/processed/karu_week3.gpkg"

The raw files were left untouched, while the processed datasets were stored separately for analysis.
