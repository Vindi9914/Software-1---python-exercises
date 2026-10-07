import random


class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"{'License plate':<15}{'Maximum speed':<15}"
              f"{'Current speed':<15}{'Distance':<15}")

        for car in self.cars:
            print(f"{car.license_plate:<15}{car.maximum_speed:<15}"
                  f"{car.current_speed:<15}{car.travelled_distance:<15}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True

        return False