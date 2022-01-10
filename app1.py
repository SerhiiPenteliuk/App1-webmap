import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elevation = list(data['ELEV'])


def color_producer(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev < 3000:
        return 'orange'
    else:
        return 'red'


map1 = folium.Map(location=[38.59, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elevation):
    fg.add_child(
        folium.CircleMarker(location=(lt, ln), radius=8, popup=str(el) + "m",
                            fill_color=color_producer(el), color='darkblue', fill_opacity=1))

fg.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                      else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                      else 'red'}))

map1.add_child(fg)
map1.save('Map1.html')
