from pyproj import Proj, transform
import json

#defineprojections
wgs84 = Proj(init = 'epsg:4326')
IrishGrid = Proj(init = 'epsg:29902')

#load in data
with open(r'/Users/hardikkhurana/Documents/GitHub/talking_network/map_files/converted_files/DmaBoundary.geojson, 'r') as f:
    data = json.load(f)

#traverse data in json string
target = []
#coord = []
f =open("Converted_file_DmaBoundary.geojson","w")
f.write("{\n")
f.write('"type": "FeatureCollection",\n')
f.write('"name": "DmaBoundary",\n')
f.write('"features": [\n')

for feature in data['features']:
     #print(feature['geometry']['type'])
     target = []
     target = feature['geometry']['coordinates']
     # objid = feature['properties']['OBJECTID']
     # diameter = feature['properties']['Diameter_m']
     # material = feature['properties']['Pipe_Mater']
     # length = feature['properties']['length_M']
     # type = feature['properties']['Type_']
     # f.write('{ "type": "Feature", "properties": { "OBJECTID": %d, "Diameter_m": "%s", "Pipe_Mater": "%s", "length_M": %d, "Type_": "%s"},' % (objid , diameter , material , length , type ))
     #print(target)
     f.write('{"type": "Feature",')
     coord = []
     # f.write('"geometry":{"type":"LineString" , "coordinates": [')
     f.write('"geometry":{"type":"Polygon", "coordinates": [')
     count = 0

     for northing in target:
         count = count+1
     flag = 0
     for northing, easting in target:
         #print "Converting", easting, northing
         # Transform using pyproj (gives wrong answer)
         flag = flag+1
         WGS84 = Proj(init='EPSG:4326')
         inp = Proj(init='EPSG:32645')
         x, y = transform(inp, WGS84, northing, easting)
         f.write('[%f,%f]' % (x,y))
         if flag < count:
             f.write(',')
         coord.append([x,y])
     f.write(']}},\n')
     print(coord)
f.write(']')
f.write('}')
f.close()
