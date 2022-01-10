import folium

# print(dir(folium))
# help(folium.Map)

Moscow = folium.Map(location=[55.7622200, 37.6155600], zoom_start=12, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

fg.add_child(
    folium.Marker(location=[55.7622200, 37.6155600], popup='Hi I am a Marker', icon=folium.Icon(color='green')))
Moscow.add_child(fg)

Moscow.save('Map1.html')
