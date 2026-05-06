import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',None)

url = 'https://raw.githubusercontent.com/jcanalesluna/bcn-geodata/master/districtes/districtes.geojson'
districts = gpd.read_file(url)
print("Table of districts data:\n", districts)
print("CRS information:\n", districts.crs)
districts

#districts = districts.to_crs(epsg = 4326, inplace = True)
districts.crs
districts.to_crs(epsg = 2062, inplace=True)
districts.crs
print("I'm not sure what this means:\n", districts)

districts["area"] = districts.area / 1000000

districts

districts["centroid"] = districts.centroid

districts

print(districts)

someStuff = Point(1052243.332, -1047096.995)
someStuff = gpd.GeoSeries(someStuff, crs = 2062)
someStuff = someStuff.to_crs(epsg = 2062)
districts["stuff_district"] = [float(someStuff.distance(centroid)) / 1000 for centroid in districts.centroid]

#ax = districts.plot(figsize = (10, 6))
ax = districts.plot(column = "NOM", figsize = (10, 6), edgecolor = "black", legend = True)
plt.show()