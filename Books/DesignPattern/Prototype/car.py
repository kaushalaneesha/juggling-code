import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object."""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object."""
        del self._objects[name]

    def clone(self, name, **attrs):
        """Clone a registered object and update its attributes."""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attrs)
        return obj

# Example class to be cloned
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def __str__(self):
        return f"{self.brand} {self.model}"

# Creating prototype instances
prototype = Prototype()
prototype.register_object("audi", Car("Audi", "A4"))
prototype.register_object("bmw", Car("BMW", "X5"))

# Cloning
audi_clone = prototype.clone("audi")
print(audi_clone)  # Output: Audi A4

bmw_clone = prototype.clone("bmw", model="M3")
print(bmw_clone)   # Output: BMW M3
