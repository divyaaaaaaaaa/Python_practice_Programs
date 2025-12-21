#accessing using value
car={"brand":"audio","fuel":"petrol"}
print(car['brand'])

#accessing using get method
car={"brand":"audio","fuel":"petrol"}
print(car.get('brand'))

#initializaing
car['color'] ="blue"
print(car)

#accesing using keys method
car_valuent=car.keys()
print(car_valuent)

#accesing using values method
car_valuent=car.values()
print(car_valuent)