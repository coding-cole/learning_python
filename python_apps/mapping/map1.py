import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[38.58,-99.00], zoom_start=6, tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=el, icon=folium.Icon(color="green")))

map.add_child(fg)
map.save("Map1.html")