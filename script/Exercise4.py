cars = 100 #number of cars available
space_in_a_car = 4.0 #number of passengers
drivers = 30 #number of drivers available for today
passengers = 90 # number of passengers for today
cars_not_driven = cars-drivers # number of empty cars can be taken by subtracting number of drivers from total number of cars
cars_driven = drivers #the total number of drivers will be the number of driven cars
car_pool_capacity = cars_driven*space_in_a_car #total number of space for passengers who can ride in car
average_passengers_per_car = passengers/cars_driven #number of average passengers
print "there are", cars, "cars available."
print "there are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", car_pool_capacity, "people today."
print "We have", passengers, "passenger to carpool today"
print "We need to put about", average_passengers_per_car, "passenger in each car."