from enum import Enum


class Fence(Enum):
    FULL = 1
    FRONT = 2
    SIDES = 3


class Garage(Enum):
    COVERED = 1
    FRONT = 2
    BACK = 3


class Laundry(Enum):
    SITE = 1
    COIN = 2
    OFF_SITE = 3


class Property:
    p_id = 0

    def __init__(self, rooms, toilets, kitchen_type, balcony, area):
        Property.p_id += 1
        self._prop_id = Property.p_id
        self._rooms = rooms
        self._toilets = toilets
        self._kitchen_type = kitchen_type
        self._balcony = balcony
        self._area = area
        self._sold = False
        self._rented = False

    @property
    def prop_id(self):
        return self._prop_id

    @property
    def rooms(self):
        return self._rooms

    @property
    def toilets(self):
        return self._toilets

    @property
    def kitchen_type(self):
        return self._kitchen_type

    @property
    def balcony(self):
        return self._balcony

    @property
    def area(self):
        return self._area

    @property
    def sold(self):
        return self._sold

    @property
    def rented(self):
        return self._rented

    @rented.setter
    def rented(self, val):
        self._rented = True

    def sell(self):
        if not self.sold:
            self._sold = True
            return True
        raise ValueError('Property already sold')

    def rent(self):
        if not self.rented:
            self._rented = True
            return True
        raise ValueError('Property already rented')

    def __repr__(self):
        return f"{self.prop_id, self.kitchen_type, self.toilets, self.area}"


class House(Property):

    def __init__(self, fencing: Fence, garage: Garage, stories: int, min_rent: int, **kwargs):
        super().__init__(**kwargs)
        self._fence = fencing
        self._garage = garage
        self._stories = stories
        self._min_rent = min_rent

    def rent(self, val):
        if val >= self._min_rent and not self.rented:
            self._rented = True
        raise ValueError('Cannot rent the house')

    def __repr__(self):
        return f"{self.__class__, self.prop_id, self.kitchen_type, self.toilets, self.area, self._fence, self._garage, self._stories}"


class Apartment(Property):

    def __init__(self, laundry: Laundry, **kwargs):
        super().__init__(**kwargs)
        self._laundry = laundry

    def rent(self, val):
        if self._laundry == Laundry.OFF_SITE and val >= 1000:
            self._rented = True
            return True

        elif self._laundry == Laundry.COIN and val >= 1300:
            self._rented = True
            return True

        elif self._laundry == Laundry.SITE and val >= 1500:
            self._rented = True
            return True
        raise ValueError('Cannot rent the property')

    def __repr__(self):
        return f"{self.__class__, self.prop_id, self.kitchen_type, self.toilets, self.area, self._laundry}"


class Interface:

    def __init__(self, property_list):
        self._property_list = property_list or []

    def list_available_property(self):
        for item in self._property_list:
            if not item.sold and not item.rented:
                print(item)

    def add_property(self, prop):

        if isinstance(prop, (House, Apartment)):
            self._property_list.append(prop)

    def sell_prop(self, prop_id):
        p = [x for x in self._property_list if x.prop_id == prop_id]
        if len(p) > 0:
            p[0].sell()
            self.list_available_property()
            return

    print('Property not found')

    def rent(self, prop_id, val):
        p = [x for x in self._property_list if x.prop_id == prop_id]
        if len(p) > 0:
            p[0].rent(val)
            self.list_available_property()
            return
        print('Property not found')


p1 = House(Fence.FRONT, Garage.BACK, 2, 1200, {1, 2, 3, 4, 5})
