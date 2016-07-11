### exercise 4 : Variables and Names

# set variable cars as 100
cars = 100

#set var space_in_a_car to 4 in float
space_in_a_car = 4.0

#set var drivers as int to 30
drivers = 30

#set var passengers
passengers = 90

#set var cars_not_driven as cars - drivers
cars_not_driven = cars - drivers

#set var cars_driven as the number of drivers
cars_driven = drivers

#set variable carpool_capacity as the number of available space
# in each car

carpool_capacity = cars_driven * space_in_a_car

#set var average_passengers_per_car as passengers
#per number of cars
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."