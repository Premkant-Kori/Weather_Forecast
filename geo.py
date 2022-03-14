from datetime import datetime
from pytz import timezone
from timezonefinder import TimezoneFinder
from sunnyday import Weather
from random import uniform
from folium import Map, Marker

class Geopoint(Marker): # Created a class
    
    #class variables
    latitude_range = (-90, 90)
    longitude_range = (-180, 180)
    
    def __init__(self, latitude, longitude): # instance method, Constructor
        #intializing Marker class
        super().__init__(location = [latitude, longitude])
        
        # Assigning some properties to the class OR definition of __init__ method
        self.latitude = latitude #instance variable
        self.longitude = longitude #instance variable
        
    def closest_parallel(self): # instance method
        # round off the value of latitude
        return round(self.latitude) # using built-in round() object
    
    def get_time(self): # instance method
        timezone_string = TimezoneFinder().timezone_at(lat=self.latitude, lng=self.longitude) # finding timezone
        time_now=datetime.now(timezone(timezone_string)) # finding current date time according to timezone_string variable
        return time_now # returning current date and time
    
    def get_weather(self): # instance method
        weather = Weather(apikey = '26631f0f41b95fb9f5ac0df9a8f43c92', lat=self.latitude, lon=self.longitude) # home.openweathermap.org/api_keys
        return weather.next_12h_simplified()
    
    @classmethod #decorator
    def random(cls): # class method
        return cls(latitude =uniform(-90, 90) , longitude = uniform(-180, 180))
    
tokyo = Geopoint(latitude = 35.7, longitude = 139.7) #instantiating Geopoint class
print(tokyo.closest_parallel()) # calling method of class
print(tokyo.get_time())
print(tokyo.get_weather())
