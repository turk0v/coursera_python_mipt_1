import csv
from os.path import splitext




class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
    def get_photo_file_ext(self):
        return splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand,photo_file_name,carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = "car"


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand,photo_file_name,carrying)
        self.body_whl = body_whl
        self.car_type = "truck"
        list_whl = self.body_whl.split('x')
        #print (list_whl)
        if len(list_whl) <= 1:
            self.body_length = 0
            self.body_width  = 0
            self.body_height = 0
        else:
            self.body_length = float(list_whl[0])
            self.body_width = float(list_whl[1])
            self.body_height = float(list_whl[2])

    def get_body_volume(self):
        return self.body_length * self.body_height * self.body_width



class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand,photo_file_name,carrying)
        self.extra = extra
        self.car_type = "spec_machine"


def get_car_list(csv_filename):
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        car_list = []  # пропускаем заголовок
        for row in reader:
            if len(row) < 7:
                continue
            else:
                if row[0] == 'car':
                    car_list.append(Car(row[1], row[3], row[5], row[2]))
                    continue
                if row[0] == 'truck':
                    car_list.append(Truck(row[1], row[3], row[5], row[4]))
                    continue
                if row[0] == 'spec_machine':
                    car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
                    continue
    #print(car_list)
    return car_list


def main():
    list = get_car_list('coursera_week3_cars.csv')
    for car in list:
        print(f'car_type {car.car_type} has __dict__ : {car.__dict__}\n')

if __name__ == '__main__':
    main()



