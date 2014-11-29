#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from pyproj import Proj
import MySQLdb

tree = ET.parse('data_open_thess.xml')
root = tree.getroot()
pnyc = Proj("+proj=tmerc +lat_0=0 +lon_0=24 +k=0.9996 +x_0=500000 +y_0=0 +ellps=GRS80 +towgs84=-199.87,74.79,246.62,0,0,0,0 +units=m +no_defs")
x = [981106.0]
y = [195544.0]
lon, lat = pnyc(x, y, inverse=True)
print lon
print lat

# for child in root:
	# print child[0].text
	# x = float(child[1].text)
	# y = float(child[2].text)
	# lon, lat = pnyc(x, y, inverse=True)
	# print lon
	# print lat
	# print child[3].text

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="*****", # your password
                      db="testing",
                      charset='utf8') # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM geo")
cur.execute("set names utf8;")  
for child in root:
	x = float(child[1].text)
	y = float(child[2].text)
	address = child[0].text
	category = child[3].text
	lon, lat = pnyc(x, y, inverse=True)
	sql = "INSERT INTO geo VALUES(\""+address+"\","+str(lat)+","+str(lon)+",\""+category[11:]+"\")"
	# print(sql)
	cur.execute(sql)
	db.commit()
	

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]