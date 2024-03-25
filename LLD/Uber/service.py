from LLD.Uber.accounts import Address


class NavigationService:
    def __init__(self) -> None:
        pass

    def navigate(self, source: Address, destination: Address):
        # Return path from source to destination
        pass


class Search:
    def __init__(self, search_query) -> None:
        self.__search_query = search_query

    def get_rides(self, search_query):
        pass