from weatherdata import *

weatherData = WeatherData()
current = CurrentConditionDisplay(weatherData)
stats = StatisticsDisplay(weatherData)
heatIndex = HeatIndexDisplay(weatherData)
weatherData.set_measurements(30, 40, 50)
weatherData.set_measurements(90, 40, 50)
weatherData.set_measurements(60, 40, 50)
