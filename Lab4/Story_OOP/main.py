from .car import Car
from .employee import Employee
from .office import Office

from .JSON_save import save_office_to_json

car1 = Car("Fiat 128", fuelRate=100, velocity=50)
emp1 = Employee("Samy", 1000, 1, car1, "samy@mail.com", 2000, 20)

office = Office("ITI Smart Village")

office.hire(emp1)

emp1.drive(20)
office.check_lateness(1, moveHour=8)

save_office_to_json(office)