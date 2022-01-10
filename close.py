import folium

# tiles = "Stamen Terrain"
Moscow = folium.Map(location=[52.353394, 31.226270], zoom_start=6)
fg = folium.FeatureGroup(name="My Map")

fg.add_child(folium.Marker(location=[55.749419, 37.383429], popup='Ksu Work', icon=folium.Icon(color='purple')))
fg.add_child(folium.Marker(location=[55.737567, 37.485096], popup='Домик Ксюши', icon=folium.Icon(color='beige')))
fg.add_child(folium.Marker(location=[48.268280, 25.939115], popup='Nast\' Home', icon=folium.Icon(color='darkblue')))
fg.add_child(folium.Marker(location=[48.272778, 25.944315], popup='My Home', icon=folium.Icon(color='orange')))
fg.add_child(folium.Marker(location=[48.272942, 25.938975], popup='Nastushka Home', icon=folium.Icon(color='pink')))
Moscow.add_child(fg)

Moscow.save('index.html')
