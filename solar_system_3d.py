import math
import matplotlib.pyplot as plt
from vectors import Vector

class SolarSystem:
    def __init__(self, size):
        self.size = size
        self.bodies = []
        self.fig = plt.figure(figsize=(8, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')
    
    def add_body(self, body):
        self.bodies.append(body)
    
    def calculate_all_body_interactions(self):
        bodies_copy = self.bodies.copy()
        for idx, first in enumerate(bodies_copy):
            for second in bodies_copy[idx + 1:]:
                first.accelerate_due_to_gravity(second)
    
    def update_all(self):
        self.bodies.sort(key=lambda item: item.position[0])
        for body in self.bodies:
            body.move()
            body.draw()
    
    def draw_all(self):
        self.ax.set_xlim((-self.size / 2, self.size / 2))
        self.ax.set_ylim((-self.size / 2, self.size / 2))
        self.ax.set_zlim((-self.size / 2, self.size / 2))
        self.ax.axis(False)
        plt.pause(0.001)
        self.ax.clear()

class SolarSystemBody:
    def __init__(self, solar_system, mass, position=(0, 0, 0), velocity=(0, 0, 0)):
        self.solar_system = solar_system
        self.mass = mass
        self.position = position
        self.velocity = Vector(*velocity)
    
    def move(self):
        self.position = tuple(map(sum, zip(self.position, self.velocity)))
    
    def draw(self):
        self.solar_system.ax.plot(
            *self.position,
            marker="o",
            markersize=self.display_size + self.position[0] / 30,
            color=self.colour
        )
    
    def accelerate_due_to_gravity(self, other):
        distance = Vector(*other.position) - Vector(*self.position)
        distance_mag = distance.get_magnitude()
        force_mag = self.mass * other.mass / (distance_mag ** 2)
        force = distance.normalize() * force_mag
        for body in (self, other):
            acceleration = force / body.mass
            body.velocity += acceleration * (-1 if body is self else 1)

class Sun(SolarSystemBody):
    def __init__(self, solar_system, mass=10_000, position=(0, 0, 0), velocity=(0, 0, 0)):
        super().__init__(solar_system, mass, position, velocity)
        self.colour = "yellow"

class Planet(SolarSystemBody):
    colours = iter([(1, 0, 0), (0, 1, 0), (0, 0, 1)])

    def __init__(self, solar_system, mass=10, position=(0, 0, 0), velocity=(0, 0, 0)):
        super().__init__(solar_system, mass, position, velocity)
        self.colour = next(Planet.colours)

