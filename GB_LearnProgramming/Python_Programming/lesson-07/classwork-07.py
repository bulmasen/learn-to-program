import staff as st


class Transport:
    horse_force = 735.49875 / 16  # watt

    def __init__(self, power_engine, mass):
        self.__power_engine_horse = power_engine
        self.__power_engine = self.__power_engine_horse * self.horse_force
        self.__mass = mass
        self._velocity = 0
        self.__tire_friction = 0.7
        self._gas_acc = self.__power_engine / self.__mass
        self.__break_acc = -9.81 / self.__tire_friction
        self.box_container = []
        self.count_box = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count_box += 1
        if self.count_box <= len(self.box_container):
            return self.box_container[self.count_box - 1]
        else:
            raise StopIteration

    def __str__(self):
        return f'\tМощность: {self.__power_engine}\n' \
               f'\tМасса: {self.__mass}\n' \
               f'\tТрение: {self.__tire_friction}\n' \
               f'\tСкорость: {self._velocity}'

    def add_box(self, item):
        if item.postcode[0] == '$' and item.postcode[1:].isdigit():
            self.box_container.append(item)

    def __iadd__(self, other):
        if isinstance(other, st.Send):
            if other.postcode[0] == '$' and other.postcode[1:].isdigit():
                self.box_container.append(other)
        return self

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

    def __str__(self):
        return f'{self.__type}' + super().__str__()


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

    def __str__(self):
        return f'{self.__type}\n' + super().__str__()


c = Car(345, 3800)
t = Truck(450, 7000, 25)

# c + Box()
# b = Box()
# c += b
# __iadd__

t.add_box(st.Box())
t.add_box(st.Box())
t.add_box(st.Box())
t.add_box(st.Box())
t.add_box(st.Box())
t.add_box(st.Box())
t.add_box(st.Box())

t += c

# for b in t.box_container:
#     print(b)

for b in t:
    print(b)
