from datetime import datetime
from timezonefinder import TimezoneFinder
from pytz import timezone
from sunnyday import Weather
from folium import Marker
from random import uniform

# terms
# class, instance, method, constructor(init)
# instance method, class method
# parameters, arguments, argument values
# instance variables, class variables
# attributes or member


class Geopoint(Marker):
    # to access class variable
    # outside class -> Geopoint.latitude_range
    # inside class -> self.latitude_range
    # can also use cls
    latitude_range = (-90, 90)
    longitude_range = (-180, 180)

    def __init__(self, latitude, longitude, popup=None):
        super().__init__(location=[latitude, longitude], popup=popup)
        self.latitude = latitude
        self.longitude = longitude

    def closest_parallel(self):
        return round(self.latitude)

    def get_time(self):
        timezonefinder = TimezoneFinder()
        # print(TimezoneFinder)
        timezone_string = timezonefinder.timezone_at(
            lng=self.longitude, lat=self.latitude
        )
        if timezone_string is None:
            return None
        else:
            tzone = timezone(timezone_string)
            time_now = datetime.now(tzone)
            return time_now

    def get_weather(self):
        # https://openweathermap.org
        weather = Weather(
            apikey="26631f0f41b95fb9f5ac0df9a8f43c92",
            lat=self.latitude,
            lon=self.longitude,
        )
        return weather.next_12h_simplified()

    @classmethod
    def random(cls):
        return cls(latitude=uniform(-90, 90), longitude=uniform(-180, 180))
