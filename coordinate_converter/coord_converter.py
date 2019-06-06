from pyproj import Proj, transform
import json

#defineprojections
wgs84 = Proj(init = 'epsg:4326')
IrishGrid = Proj(init = 'epsg:29902')

#load in data
with open(r'C:\Users\khurana-hardik\Documents\talking_network\trial.geojson', 'r') as f:
    data = json.load(f)

#traverse data in json string
target = []
#coord = []
f =open("trial.txt","w")
f.write("{\n")
f.write('"type": "FeatureCollection",\n')
f.write('"name": "Existing_Pipe",\n')
f.write('"features": [\n')

for feature in data['features']:
     #print(feature['geometry']['type'])
     target = []
     target = feature['geometry']['coordinates']
     objid = feature['properties']['OBJECTID']
     diameter = feature['properties']['Diameter_m']
     material = feature['properties']['Pipe_Mater']
     length = feature['properties']['length_M']
     type = feature['properties']['Type_']
     f.write('{ "type": "Feature", "properties": { "OBJECTID": %d, "Diameter_m": %s, "Pipe_Mater": %s, "length_M": %s, "Type_": %s},' % (objid , diameter , material , length , type ))
     #print(target)
     coord = []
     f.write('"geometry":{"type":"LineString" , "coordinates": [')
     for northing, easting in target:
         #print "Converting", easting, northing
         # Transform using pyproj (gives wrong answer)
         WGS84 = Proj(init='EPSG:4326')
         inp = Proj(init='EPSG:32645')
         x, y = transform(inp, WGS84, northing, easting)
         f.write('[%f,%f]' % (x,y))
         coord.append([x,y])
     f.write(']}')
     print(coord)
