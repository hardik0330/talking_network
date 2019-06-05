import folium
import os
import json

m = folium.Map(location=[22.5726, 88.3639], zoom_start=12)

overlay = os.path.join('Existing_Pipe2.json')

# geojson overlay
folium.GeoJson(overlay, name='Kolkata').add_to(m)

folium.Marker([64.14604223999996, 25.00966851399999],
              popup='<strong>Location two</strong>',
              icon=folium.Icon(icon='cloud')).add_to(m)

m.save('map.html')
