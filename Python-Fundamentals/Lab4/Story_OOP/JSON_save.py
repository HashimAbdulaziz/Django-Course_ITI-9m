import json

def save_office_to_json(office, filename="office.json"):
    data = []

    for emp in office.employees:
        data.append({
            "id": emp.id,
            "name": emp.name,
            "salary": emp.salary,
            "email": emp.email,
            "car": emp.car.name,
            "fuelRate": emp.car.fuelRate
        })

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)