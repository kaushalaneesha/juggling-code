import xml.etree.ElementTree as etree
import json

class JsonConnector:
    def __init__(self, filepath) -> None:
        self.__data = dict()
        with open(filepath, mode = 'r', encoding='utf-8') as f:
            self.__data = json.load(f)

    @property
    def parsed_data(self):
        return self.__data
    

class XMLConnector:
    def __init__(self, filepath) -> None:
        self.__tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.__tree

# Factory method and class having the logic to create object based on what we want   
class ConnectorFactory:
    def get_connection(self, filepath):
        if filepath.endswith('json'):
            connector = JsonConnector
        elif filepath.endswith('xml'):
            connector = XMLConnector
        else:
            raise ValueError('Cannot connect to {}'.format(filepath))
        return connector(filepath)

# Create 1 instance of factory
factory = ConnectorFactory()

# Creates the object and returns the data depending on the kind of connection, using factory method 
class ObjectConnector:
    def get_parsed_data(self, filepath):
        try:
            connector = factory.get_connection(filepath)
            return connector.parsed_data
        except ValueError as ex:
            print(ex)
            return None
        

############################################################################################
        
connector = ObjectConnector()
parsed_data = connector.get_parsed_data("/Users/anek/Documents/Interview Questions/Pratice/Books/DesignPattern/FactoryMethod/data/person.xml")


# XML Parsing
persons = parsed_data.findall("person")
print('found: {} persons'.format(len(persons)))
for person in persons:
    print('first name: {}'.format(person.find('firstName').text))
    print('last name: {}'.format(person.find('lastName').text))
    [print('phone number ({}):'.format(p.attrib['type']), p.text) for p in person.find('phoneNumbers')]

# JSON parsing
parsed_data = connector.get_parsed_data("/Users/anek/Documents/Interview Questions/Pratice/Books/DesignPattern/FactoryMethod/data/donut.json")
print('found: {} donuts'.format(len(parsed_data)))
for donut in parsed_data:
    print('name: {}'.format(donut['name']))
    print('price: ${}'.format(donut['ppu']))
    [print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']] 
