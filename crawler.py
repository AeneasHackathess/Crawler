import xml.etree.ElementTree as ET
from pyproj import Proj

tree = ET.parse('data_open_thess.xml')
root = tree.getroot()
pnyc = Proj("+proj=tmerc +lat_0=0 +lon_0=24 +k=0.9996 +x_0=500000 +y_0=0 +ellps=GRS80 +towgs84=-199.87,74.79,246.62,0,0,0,0 +units=m +no_defs")
x = [981106.0]
y = [195544.0]
lon, lat = pnyc(x, y, inverse=True)
print lon
print lat

for child in root:
	print child[0].text
	x = float(child[1].text)
	y = float(child[2].text)
	lon, lat = pnyc(x, y, inverse=True)
	print lon
	print lat
	print child[3].text