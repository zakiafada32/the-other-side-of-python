from folium import Map, Popup
from .geo import Geopoint

# Get latitude and longitude values
locations = [[1, -1], [2, 2], [39, 5], [42, 1]]

# Folium Map instance
mymap = Map(location=[40, 2])

for lat, lon in locations:
    # Create a Geopoint instance
    geopoint = Geopoint(latitude=lat, longitude=lon)
    forecast = geopoint.get_weather()
    popup_content = f"""
    {forecast[0][0][-8:-6]}h: {round(forecast[0][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[1][0][-8:-6]}h: {round(forecast[1][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[2][0][-8:-6]}h: {round(forecast[2][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png" width=35>
    <hr style="margin:1px">
    {forecast[3][0][-8:-6]}h: {round(forecast[3][1])}°F <img src="http://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png" width=35>
    """
    # Create Popup object and add it to Geopoint
    popup = Popup(popup_content, max_width=400)
    popup.add_to(geopoint)
    geopoint.add_to(mymap)

# Save the Map instance into a HTML file
mymap.save("maps/map.html")