from solar_system_3d import SolarSystem, Sun, Planet

solar_system = SolarSystem(400)

sun = Sun(solar_system)
solar_system.add_body(sun)

planet1 = Planet(solar_system, position=(150, 50, 0), velocity=(0, 5, 5))
solar_system.add_body(planet1)

planet2 = Planet(solar_system, mass=20, position=(100, -50, 150), velocity=(5, 0, 0))
solar_system.add_body(planet2)

while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()
