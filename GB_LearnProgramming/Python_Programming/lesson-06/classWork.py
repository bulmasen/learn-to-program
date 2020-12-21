class Transport:
    horse_force = 735.49875/16  # watt

    def __init__(self, power_engine, mass):
        self.__power_engine = power_engine*self.horse_force
        self.__mass = mass
        self._velocity = 0
        self.__tire_friction = 0.7
        self._gas_acc = self.__power_engine/self.__mass
        self.__break_acc = -9.81 / self.__tire_friction

    def gas_pedal(self, duration):
        rez = ""
        for time in range(duration):
            velocity = self._velocity + time * self._gas_acc
            rez += f"{velocity:.0f} "
        self._velocity = velocity
        return rez

    def break_pedal(self, duration=None):
        rez = ""
        for time in range(duration):
            velocity = self._velocity + time * self.__break_acc
            if velocity <= 0:
                rez += f"[stop]"
                break
            else:
                rez += f"{velocity:.0f} "
        self._velocity = velocity
        return rez

    def speedometer(self):
        return self._velocity


class Car(Transport):
    def __init__(self, power_engine, mass):
        self.__type = "car"
        super().__init__(power_engine, mass)


class Truck(Transport):
    def __init__(self, power_engine, mass, velocity_limit=None):
        self.__type = "truck"
        self.velocity_limit = velocity_limit
        super().__init__(power_engine, mass)

    def gas_pedal(self, duration):
        rez = ""
        for time in range(duration):
            velocity = self._velocity + time * self._gas_acc
            if self.velocity_limit is not None and velocity >= self.velocity_limit:
                rez += f"{self.velocity_limit} [limit]"
                break
            else:
                rez += f"{velocity:.0f} "
        self._velocity = velocity
        return rez


c = Car(345, 3800)
t = Truck(450, 7000, 25)

print(c.gas_pedal(18))
print(t.gas_pedal(14))
