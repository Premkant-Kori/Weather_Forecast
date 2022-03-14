from folium import Map, Marker, Popup
from geo import Geopoint 

# Get latitude and longitude values
latitude = 40.4 #object instance of float type
longitude = -3.7 #object instance of float type

# Folium Map instance
mymap = Map(location = [latitude, longitude]) # Map object instance created by map type

# Created a Geopoint instance
geopoint = Geopoint(latitude=latitude, longitude=longitude)

forecast=geopoint.get_weather()

popup_content = f"""
{forecast[0][0][-8:-6]}h: {round(forecast[0][1])}° <img src="https://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png"  width=35> {forecast[0][2]}
<hr style="margin:1px">
{forecast[1][0][-8:-6]}h: {round(forecast[1][1])}° <img src="https://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png" width=35> {forecast[1][2]}
<hr style="margin:1px">
{forecast[2][0][-8:-6]}h: {round(forecast[2][1])}° <img src="https://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png" width=35> {forecast[2][2]}
<hr style="margin:1px">
{forecast[3][0][-8:-6]}h: {round(forecast[3][1])}° <img src="https://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png" width=35> {forecast[3][2]}
"""

popup=Popup(popup_content, max_width=400)
popup.add_to(geopoint)
geopoint.add_to(mymap)

#save the Map instance into a HTML file
mymap.save("map.html")
