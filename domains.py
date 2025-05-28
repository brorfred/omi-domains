import folium
from folium.plugins import MarkerCluster
from folium.plugins import MousePosition

import pandas as pd

#Define coordinates of where we want to center our map
boulder_coords = [0.0, 0.0]

#Create the map
gog_map = folium.Map(location = boulder_coords,
                     tiles="Esri.OceanBasemap",
                     zoom_start = 5)

kw = dict(
    color="blue",
    line_cap="round", line_join="round",
    dash_array="5, 5",
    fill=True, fill_color="blue",
    weight=1,
    #"popup": "Tokyo, Japan",
    )

folium.Rectangle(
    bounds=[[-1, -10], [7, 10]],
    tooltip="Gulf of Guinea lon:-10° - 10°, lat:-1° – 7°",
    **kw,
).add_to(gog_map)

folium.Rectangle(
    bounds=[[2, -3], [6.6, 6]],
    tooltip="Upwelling region lon:-3° - 6°, lat:2° – 6.6°",
    **kw,
).add_to(gog_map)


folium.Rectangle(
    bounds=[[5, -0.5], [6, 0.5]],
    tooltip="Field stations lon:-0.5° - 0.5°, lat:5° – 6°",

    **kw,
).add_to(gog_map)

url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
country_shapes = f'{url}/world-countries.json'
folium.Choropleth(
    geo_data=country_shapes,
    name='choropleth',
    #data=orders_by_country,
    columns=['country', 'orders'],
    key_on='feature.id',
    fill_color='Blues',
    nan_fill_color='white',
    fill_opacity=0.0,
    line_opacity=0.2,
    line_weight=2
).add_to(gog_map)
MousePosition().add_to(gog_map)

#harbour_cluster = MarkerCluster().add_to(gog_map)
#folium.Marker(location=[5.635930,  0.016836], tooltip="Tema").add_to(harbour_cluster)
#folium.Marker(location=[5.775000,  0.272000], tooltip="Ayitepa").add_to(harbour_cluster)
#folium.Marker(location=[5.709084,  0.119025], tooltip="Prampram").add_to(harbour_cluster)
#folium.Marker(location=[5.613657, -0.048219], tooltip="Sakumono").add_to(harbour_cluster)
#folium.Marker(location=[5.534867, -0.210368], tooltip="Jamestown").add_to(harbour_cluster)


#Display the map
gog_map.save("docs/index.html")
