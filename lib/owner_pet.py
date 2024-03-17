class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        type(self).all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception(
                f"Invalid pet type: {pet_type}. Must be one of: {', '.join(self.PET_TYPES)}"
            )
        self._pet_type = pet_type

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if owner and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner")
        self._owner = owner


class Owner:

    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise ValueError("Provided pet must be an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
