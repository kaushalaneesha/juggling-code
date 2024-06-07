from abc import ABC

class Observer(ABC):
    def update(self, temperature, humidity, pressure):
        pass

class Display(ABC):
    def display(self):
        pass

class Subject(ABC):
    def __init__(self):
        super().__init__()
        self._observers = []

    def addObserver(self, observer: Observer):
        self._observers.append(observer)

    def removeObserver(self, observer: Observer):
        self._observers.remove(observer)

   

class WeatherData(Subject):
    def __init__(self) -> None:
        self._temp = None
        self._humidity = None
        self._pressure = None
        self._observers = []  # Initialize _observers list

    def measurementChanged(self):
        self.notifyObservers()

    def set_measurements(self, temp, humidity, pressure):
        self._temp = temp
        self._humidity = humidity
        self._pressure = pressure
        self.measurementChanged()

    def notifyObservers(self):
        for observer in self._observers:
            observer.update(self._temp, self._humidity, self._pressure)

class CurrentConditionDisplay(Display, Observer):
    def __init__(self, weatherData: Subject) -> None:
        self._temp = None
        self._humidity = None
        self._pressure = None
        self._weatherData = weatherData
        self._weatherData.addObserver(self)

    def display(self):
        print("Current condition display {} {} {}".format(self._temp, self._humidity, self._pressure))

    def update(self, temp, humidity, pressure):
        self._humidity = humidity
        self._temp = temp
        self._pressure = pressure
        self.display()

class StatisticsDisplay(Display, Observer):
    def __init__(self, weatherData: Subject) -> None:
        self._temp = None
        self._humidity = None
        self._pressure = None
        self._weatherData = weatherData
        self._weatherData.addObserver(self)

    def display(self):
        print("Statistics Display {} {} {}".format(self._temp, self._humidity, self._pressure))

    def update(self, temp, humidity, pressure):
        self._humidity = humidity
        self._temp = temp
        self._pressure = pressure
        self.display()

class HeatIndexDisplay(Display, Observer):
    def __init__(self, weatherData: Subject) -> None:
        self._temp = None
        self._humidity = None
        self._pressure = None
        self._weatherData = weatherData
        self._weatherData.addObserver(self)

    def display(self):
        print("Heat Index is {}".format(self._temp * .8))

    def update(self, temp, humidity, pressure):
        self._humidity = humidity
        self._temp = temp
        self._pressure = pressure
        self.display()


