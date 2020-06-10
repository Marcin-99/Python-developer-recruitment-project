from exceptions import IllegalCarError


class Car:
    def __init__(self, pax_count, car_mass, gear_count):
        if pax_count < 1:
            raise IllegalCarError(f"pax_count should be greater or equal to 1, {pax_count} was given.")
        if pax_count > 5:
            raise IllegalCarError(f"pax_count should be smaller or equal to 1, {pax_count} was given.")
        if car_mass > 2000:
            raise IllegalCarError(f"car_mass should be smaller or equal to 2000, {car_mass} was given.")
        self._pax_count = pax_count
        self._car_mass = car_mass
        self._gear_count = gear_count
        self._total_mass = car_mass + pax_count * 70

    @property
    def pax_count(self):
        return self._pax_count

    @property
    def car_mass(self):
        return self._car_mass

    @property
    def gear_count(self):
        return self._gear_count

    @property
    def total_mass(self):
        return self._total_mass

    @pax_count.setter
    def pax_count(self, new_value):
        if new_value < 1:
            raise IllegalCarError(f"pax_count should be greater or equal to 1, {new_value} was given.")
        if new_value > 5:
            raise IllegalCarError(f"pax_count should be smaller or equal to 1, {new_value} was given.")
        self._pax_count = new_value

    @car_mass.setter
    def car_mass(self, new_value):
        if new_value > 2000:
            raise IllegalCarError(f"car_mass should be smaller or equal to 2000, {new_value} was given.")
        self._car_mass = new_value
        self._total_mass = self.car_mass + self.pax_count * 70
