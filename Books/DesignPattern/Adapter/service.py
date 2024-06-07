# Third party service which client doesnt have access to
class ThirdPartyService:
    def __init__(self) -> None:
        pass

    def special_feature(self):
        return "laiceps erutaef a si sihT"

class Target:
    def __init__(self) -> None:
        pass

    def normal_request(self):
        return "This was always used by client"

class Adapter(Target):
    def __init__(self, service: ThirdPartyService) -> None:
        super().__init__()
        self.__service = service

    def normal_request(self):
        return self.__service.special_feature()[::-1]

# Client code
def client_code(target: Target) -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.normal_request())

target = Target()
client_code(target)

service = ThirdPartyService()
print(service.special_feature()) # not clear


adpater = Adapter(service)
client_code(adpater)


