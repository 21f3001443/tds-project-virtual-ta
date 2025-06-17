## Geospatial Analysis with QGIS

[![Geospatial analysis with QGIS](https://i.ytimg.com/vi_webp/tJhehs0o-ik/sddefault.webp)](https://youtu.be/tJhehs0o-ik
<youtube_summary>This tutorial explains how to use QGIS, a free and open-source geographic information system, to create shapefiles and KML files for storing geographic and demographic information. Shapefiles for countries, cities, and states can often be downloaded from websites like Diva-GIS, but when unavailable, users can create shapefiles in QGIS.

To start, users download QGIS from its official website, choosing the appropriate version (32-bit or 64-bit) for Windows, Mac, or Linux. Upon opening QGIS, important toolbars such as the digitizing toolbar and panels like the browser and layers panels should be enabled via the View menu if not visible.

The tutorial demonstrates downloading Sudan's shapefiles from Diva-GIS, showing multiple administrative levels (country, state, district, city). However, the available shapefile only includes North Sudan, lacking South Sudan, which became independent in 2011.

QGIS features allow inspecting shapefile attributes via the attribute table, displaying names for different administrative levels and potential demographic data. Users can customize shapefile appearance by changing colors and adding labels to display attribute names on the map.

A useful plugin, Quick Map Services, can be installed to overlay shapefiles on a world map using sources like OpenStreetMap. This helps visualize the geographic context, confirming South Sudan’s absence in the downloaded shapefile.

To create a shapefile for South Sudan, the tutorial guides users to remove the existing North Sudan layers, then create a new polygon shapefile named "South Sudan" with attributes such as ID and name. Using the digitizing toolbar, users toggle editing mode, draw the polygon approximating South Sudan’s borders, and assign attribute values.

Once created, the shapefile can be exported in various formats, including shapefile and KML. The KML file can be opened in Google Earth, showing the newly created South Sudan boundary with associated attribute information visible upon clicking the area.

In summary, this tutorial covers downloading existing shapefiles, exploring their attributes, customizing visualization, installing helpful plugins, and creating new shapefiles in QGIS when data is missing, demonstrated through creating South Sudan's shapefile and exporting it as both shapefile and KML formats.</youtube_summary>
)

You'll learn how to use QGIS for geographic data processing, covering:

- **Shapefiles and KML Files**: Create and manage shapefiles and KML files for storing and analyzing geographic information.
- **Downloading QGIS**: Install QGIS on different operating systems and familiarize yourself with its interface.
- **Geospatial Data**: Access and utilize shapefiles from sources like Diva-GIS and integrate them into QGIS projects.
- **Creating Custom Shapefiles**: Learn how to create custom shapefiles when existing ones are unavailable, including creating a shapefile for South Sudan.
- **Editing and Visualization**: Use QGIS tools to edit shapefiles, add attributes, and visualize geographic data with various styling and labeling options.
- **Exporting Data**: Export shapefiles or KML files for use in other applications, such as Google Earth.

Here are links used in the video:

- [QGIS Project](https://www.qgis.org/en/site/)
- [Shapefile Data](https://www.diva-gis.org/gdata)
