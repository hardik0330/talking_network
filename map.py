import folium
import os
import json

m = folium.Map(location=[22.594264, 88.368343], zoom_start=13)

overlay = os.path.join(
    '/home/vinayakk/suez_internship/talking_network/coordinate_converter/Converted_file.geojson')

# geojson overlay
folium.GeoJson(overlay, name='Kolkata').add_to(m)

m.save('map.html')
