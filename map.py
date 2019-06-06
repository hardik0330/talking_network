import folium
import os
import json

m = folium.Map(location=[22.594264, 88.368343], zoom_start=13)

overlay = os.path.join('Existing_Pipe2.json')

# geojson overlay
folium.GeoJson(overlay, name='Kolkata').add_to(m)

m.save('map.html')
