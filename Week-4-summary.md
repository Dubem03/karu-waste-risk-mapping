Month 1 Summary - Spatial Analysis

Project Question

How does the location of waste dumpsites in Karu LGA relate to surrounding settlements and potential population exposure?

Spatial Operation

For Week 4, I used a buffer operation to investigate the area surrounding identified waste points in Karu LGA.

I selected the buffer operation because my question involves distance from waste locations. A buffer creates a defined area around each waste point, allowing me to identify settlements and other features that fall within a specified distance of the waste locations.

The analysis was carried out using the projected EPSG:32632 (WGS 84 / UTM Zone 32N) coordinate reference system prepared during Week 3. This was necessary because the buffer distance is measured in metres.

Expected Result

I expected the buffer operation to create a defined zone around each waste point. I expected the resulting buffer areas to show which parts of the surrounding area, including nearby settlements, may fall within the selected distance from the waste locations.

I also expected the output to contain the same number of waste-point features as the input where the buffers were created without dissolving overlapping features.

What I Got

The buffer operation successfully produced buffer geometries around the waste points using a distance measured in metres.

The resulting layer can be used to compare the waste locations with surrounding settlement data and identify areas that fall within the selected distance.

The analysis result was checked by viewing the output on the map and inspecting the attribute table. I also checked individual buffer features against their corresponding waste points.

What Surprised Me

One challenge during the analysis was that some of the supporting settlement data required for the final map was not yet available in the form needed for the analysis.

This showed me that a spatial operation can be completed successfully while the interpretation of the result can still depend on having the appropriate supporting datasets.

I therefore treated the current buffer output as an intermediate analysis result and will add the settlement layer when the missing data is available.

Data Still Needed

The main data I still need is the appropriate settlement/populated-place dataset for Karu LGA. This will allow me to overlay settlements on the waste-point buffers and examine which settlements fall within the selected distance from waste locations.

Additional supporting datasets may also be used later to improve the analysis, depending on availability.

Week 4 Conclusion

The Week 4 practical helped me move from simply preparing GIS data to performing a spatial analysis based on a real project question.

The buffer operation provides the first spatial relationship needed for my waste-risk mapping project. The next step is to combine the buffer output with settlement data and interpret the areas potentially exposed based on distance from waste locations.
