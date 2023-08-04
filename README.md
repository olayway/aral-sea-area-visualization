Aral Sea Area Visualization using Satellite Imagery via Google Earth Engine

The main goal of this project is to visualize the changes in the Aral Sea's area from 1986 to 2023 using satellite shots available in Google Earth Engine. We aim to extract good quality images of the Aral Sea during this period and apply light Photoshop techniques to reduce clouds and ensure color consistency across different satellites.

Satellites used:
- 1986-2000, 2006-2011: USGS Landsat 5 Level 2, Collection 2, Tier 1
- 2001-2005, 2012: USGS Landsat 7 Level 2, Collection 2, Tier 1
- 2013-2021: USGS Landsat 8 Level 2, Collection 2, Tier 1
- 2022-2023: USGS Landsat 9 Level 2, Collection 2, Tier 1

Data Collection and Processing:
To obtain the images, we used 'main.py' with the Earth Engine API and geemap in Google Colab. Running the code in this environment is recommended as the API is already installed by default, and it provides better integration with the map viewer.

After obtaining the images, we utilized the Healing Brush tool and color matching in Adobe Photoshop to enhance consistency between pictures taken over the years. While the brush sacrifices some land details, the scope of this project focuses on the water area, which has remianed largely untouched after the edits. Additionally, we employed DaVinci Resolve to create smooth transitions between the images, color match and brighten them, add year and area data, and finalize the video editing.

Data Sources:
- Water area data for the Aral Sea is sourced from the UNESCO study 'Aral Sea and the Aral Region': [https://unesdoc.unesco.org/ark:/48223/pf0000374223]
- Data beyond 2018 is limited and was manually collected from various national and international news articles and studies found across the Internet.

Scripts Overview:
- main.py contains everything for obtaining the initial images from the Google Earth Engine
- aral_graph.py contains the matplotlib code to build a line graph based on the UNESCO data

Data Overview:
- 'aral_area.csv': CSV file containing water area data based on UNESCO records
- 'aral_mosaics_raw.zip': Folder with initial images collected via 'main.py'
- 'aral_mosaics_edited.zip': Folder with images after post-processing in Photoshop

Comparison between raw and edited images for [year]:

![Screenshot 2023-08-04 at 10 58 32](https://github.com/open-data-kazakhstan/aral-sea-area-visualization/assets/109875855/821115c2-4fc1-43fb-ad3e-98b1852d54ea)

Resulting line graph:

![Screenshot 2023-08-02 181413](https://github.com/open-data-kazakhstan/aral-sea-area-visualization/assets/109875855/62129937-bcf6-4eb8-a456-e0ff87d445a8)

Please feel free to contribute to this research project and help us in visualizing the changes in the Aral Sea over time. Your input is valuable to us!
