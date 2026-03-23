import re
from .person import Person

class Employee(Person):

    def __init__(self, name, money, emp_id, car, email, salary, distanceToWork):
        super().__init__(name, money)

        self.id = emp_id
        self.car = car
        self.distanceToWork = distanceToWork
        self.email = email if self.validate_email(email) else None
        self.salary = max(salary, 1000)

    def validate_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"


    def drive(self, distance):
        self.car.run(self.car.velocity, distance)


    def refuel(self, gasAmount=100):
        self.car.fuelRate = min(100, self.car.fuelRate + gasAmount)


    def send_mail(self, to, subject, msg, receiver_name):
        print(f"""
        To: {to}
        Subject: {subject}
        Dear {receiver_name},
        {msg}
        """)