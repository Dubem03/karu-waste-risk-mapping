# Week 4 - Buffer Analysis

## Spatial Analysis

I used a **buffer operation** to examine the areas surrounding identified waste disposal points.

The analysis was performed using **EPSG:32632 (WGS 84 / UTM Zone 32N)**, allowing buffer distances to be measured in metres.

The following proximity zones were created:

- 0-250 m
- 250-500 m
- 500 m-1 km
- 1-2 km
- Greater than 2 km

The buffer output was used to identify areas surrounding the waste disposal points that fall within the selected distances.

### Preliminary Settlement Results

| Buffer distance | Settlement count |
|---|---:|
| 250 m | 1,674 |
| 500 m | 4,868 |
| 1 km | 16,098 |
| 2 km | 52,853 |

These results represent **potential exposure based on spatial proximity** to waste disposal points. They do not confirm contamination or direct health risk
## Map Output

The map shows the identified waste disposal points and their surrounding buffer zones, providing a visual representation of the spatial relationship between waste locations and nearby areas.
