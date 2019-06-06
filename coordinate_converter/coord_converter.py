from pyproj import Proj, transform
import json

#defineprojections
wgs84 = Proj(init = 'epsg:4326')
IrishGrid = Proj(init = 'epsg:29902')

#load in data
with open(r'C:\Users\khurana-hardik\Documents\talking_network\Existing_Pipe.geojson', 'r') as f:
    data = json.load(f)

#traverse data in json string
target = []
#coord = []
for feature in data['features']:
     #print(feature['geometry']['type'])
     target = []
     target = feature['geometry']['coordinates']
     #print(target)
     coord = []

     for northing, easting in target:
         #print "Converting", easting, northing
         # Transform using pyproj (gives wrong answer)
         WGS84 = Proj(init='EPSG:4326')
         inp = Proj(init='EPSG:32645')
         x, y = transform(inp, WGS84, northing, easting)
         coord.append([x,y])
     print(coord)
