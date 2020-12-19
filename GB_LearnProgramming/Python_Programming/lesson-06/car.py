class Car():

    horse_force = 735.49875 / 16  # watt

    def __init__(self, engine, mass, friction):
        self.engine = engine
        self.mass = mass
        self.friction = friction
        self.gas_acc = self.engine / self.mass
        self.break_acc = -9.81 / self.friction

        self.velocity = 0

    def gas_pedal(self, duration):
        rez = ''
        for time in range(duration):
            velocity = self.velocity + time * self.gas_acc
            rez += f'{velocity:.0f} '
        self.velocity = velocity
        return rez

    def break_pedal(self, duration):
        print(f'Вы нажали на педаль газа {duration} сек')

    def speedometer(self):
        return self.velocity


car1 = Car(345, 2500, 0.7)
car2 = Car(250, 3800, 0.5)

print(car1.engine)
car1.gas_pedal(12)
