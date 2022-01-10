import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elevation = list(data['ELEV'])

map1 = folium.Map(location=[38.59, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elevation):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el) + "m", icon=folium.Icon(color='purple')))
map1.add_child(fg)

map1.save('Map1.html')
