from car import Car

car = Car("Ferrari", 12)

print(car.model)
print(car.consumption)
print(car.gas_tank)

car.get_gas(50)

print(car.gas_tank)

car.travel(120)

print(car.gas_tank)