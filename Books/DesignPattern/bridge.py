from abc import ABC


class Remote:
    def __init__(self, device) -> None:
        self.__device = device

    def toogle_power(self):
        if self.__device.is_enabled:
            self.__device.disable()
        else:
            self.__device.enable()

    def volume_up(self):
        self.__device.volume = self.__device.volume + 10
                                 
    def volume_down(self):
        self.__device.set_volume(self.__device.getVolume() - 10)

class Device(ABC):
    def __init__(self) -> None:
        self._volume = 10
        self.is_enabled = False

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):
        print("setting volume to {}".format(value))
        self._volume = value

    def enable(self):
        print("enabled")
        self.is_enabled = True

    def disable(self):
        print("disabled")
        self.is_enabled = False

class TV(Device):
    pass

tv = TV()
remote = Remote(tv)
remote.toogle_power()
remote.volume_up()



    