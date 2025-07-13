import json


class Person:
    def __init__(self, name, age):
        self._name = name  # protected
        self._age = age  # protected

    def greet(self):
        print(f"NAME: {self._name}")
        print(f"AGE: {self._age}")


class Staff(Person):
    def __init__(self, name, age, staff_id):
        super().__init__(name, age)
        self.staff_id = staff_id

    def greet(self):
        print(f"NAME: {self._name}")
        print(f"AGE: {self._age}")
        print(f"STAFF ID: {self.staff_id}")

    def to_dict(self):
        return {
            "name": self._name,
            "age": self._age,
            "staff_id": self.staff_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"], data["staff_id"])


class Customer(Person):
    def __init__(self, name, age, customer_id):
        super().__init__(name, age)
        self.customer_id = customer_id

    def greet(self):
        print(f"NAME: {self._name}")
        print(f"AGE: {self._age}")
        print(f"CUSTOMER ID: {self.customer_id}")

    def to_dict(self):
        return {
            "name": self._name,
            "age": self._age,
            "customer_id": self.customer_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"], data["customer_id"])


class Vehicle:
    def __init__(self, vehicle_id, model, company, price, status):
        self._vehicle_id = vehicle_id
        self._model = model
        self._company = company
        self._price = price
        self._status = status

    def display(self):
        print(f"Vehicle ID: {self._vehicle_id}")
        print(f"Model : {self._model}")
        print(f"Company : {self._company}")
        print(f"Price : {self._price}")
        print(f"Status : {self._status}")

    def vehicle_id(self):
        return self._vehicle_id

    def set_status(self, value):
        self._status = value

    def get_status(self):
        return self._status


class Car(Vehicle):
    def __init__(self, vehicle_id, model, company, price, status, type):
        super().__init__(vehicle_id, model, company, price, status)
        self.type = type

    def display(self):
        print(f"Vehicle ID: {self._vehicle_id}")
        print(f"Model : {self._model}")
        print(f"Company : {self._company}")
        print(f"Price : {self._price}")
        print(f"Status : {self._status}")
        print(f"Type : {self.type}")

    def to_dict(self):
        return {
            "vehicle_id": self._vehicle_id,
            "model": self._model,
            "company": self._company,
            "price": self._price,
            "status": self._status,
            "type": self.type
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["vehicle_id"], data["model"], data["company"], data["price"], data["status"], data["type"])


class Bike(Vehicle):
    def __init__(self, vehicle_id, model, company, price, status, type):
        super().__init__(vehicle_id, model, company, price, status)
        self._type = type

    def display(self):
        print(f"Vehicle ID: {self._vehicle_id}")
        print(f"Model : {self._model}")
        print(f"Company : {self._company}")
        print(f"Price : {self._price}")
        print(f"Status : {self._status}")
        print(f"Type : {self._type}")

    def to_dict(self):
        return {
            "vehicle_id": self._vehicle_id,
            "model": self._model,
            "company": self._company,
            "price": self._price,
            "status": self._status,
            "type": self._type
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["vehicle_id"], data["model"], data["company"], data["price"], data["status"], data["type"])


staff = []
customer = []
cars = []
bikes = []
booking = []


# cout <<"YOLO C++ LOL PYTHON SUCKS LOL ""<< endl;
# int arr[5] == int * arr = new arr[5]

def add_customers():
    name = input("Enter Your Name: ")
    age = int(input("Enter your Age: "))
    customer_id = int(input("Enter Customer ID: "))
    cust = Customer(name, age, customer_id)
    customer.append(cust)
    print("Customer Added Successfully!")


def add_staff():
    name = input("Enter Your Name: ")
    age = int(input("Enter Your Age: "))
    staff_id = int(input("Enter Your Staff ID: "))
    stf = Staff(name, age, staff_id)
    staff.append(stf)
    print("Staff Added Successfuly!")


def welcome_menu():
    print("==[- Welcome to the Car Management System -]==")
    print("1) CUSTOMER OPTIONS")
    print("2) STAFF OPTIONS")
    print("3) REGISTER AS CUSTOMER")
    print("4) REGISTER AS STAFF")
    print("0) Exit")


def customer_menu():
    print("  ==[- CUSTOMER MENU -]== ")
    print("1. View Available Vehicles")
    print("2. Book a Vehicle")
    print("3. Return Vehicle")
    print("4. My Booking History")
    print("0. Go Back")
    print("  -----------------------")


def staff_menu():
    print(" ==[- STAFF MENU -]== ")
    print("1. Add Vehicle to Inventory")
    print("2. View All Vehicles")
    print("3. Update Vehicle Status")
    print("4. Remove Vehicle from Inventory")
    print("5. View Booking History")
    print("0. Go back")
    print("-----------------------")


# CUSTOMER FUNCTIONS
def available_vehicles():
    print("[== VEHICLES LIST ==]")
    print("[-- CAR LIST --]")
    for car in cars:
        if car.get_status():
            car.display()
    print("----------------")
    print("[-- BIKE LIST --]")
    for bike in bikes:
        if bike.get_status():
            bike.display()
    print("----------------")
    print("==================")


def book_vehicle():
    customer_id = int(input("Enter the customer ID: "))
    vehicle_id = int(input("Enter the Vehicle  ID: "))

    found = False
    for car in cars:
        if vehicle_id == car.vehicle_id() and car.get_status():
            car.set_status(False)
            booking.append([customer_id, vehicle_id])
            print("Car Booked Successfully")
            found = True
            break

    for bike in bikes:
        if vehicle_id == bike.vehicle_id() and bike.get_status():
            bike.set_status(False)
            booking.append([customer_id, vehicle_id])
            print("Bike Booked Successfully")
            found = True
            break

    if not found:
        print("Vehicle not available or invalid ID.")


def return_vehicle():
    customer_id = int(input("Enter Your Customer ID: "))
    vehicle_id = int(input("Enter Vehicle ID: "))
    for car in cars:
        if vehicle_id == car.vehicle_id() and not car.get_status():
            car.set_status(True)
            break
    for bike in bikes:
        if vehicle_id == bike.vehicle_id() and not bike.get_status():
            bike.set_status(True)
            break
    for b in booking:
        if b[0] == customer_id and b[1] == vehicle_id:
            booking.remove(b)
            print("Vehicle Removed Successfully!")
            return

    print("No booking record found for this customer and vehicle.")


# STAFF FUNCTIONS
def add_vehicle():
    print("1. ADD A CAR")
    print("2. ADD A BIKE")
    print("0. GO BACK")
    print("--------------")
    choice = int(input("Enter a choice: "))
    if choice == 1:  # vehicle_id, model, company, price, status, type
        vehicle_id = int(input("Enter Vehicle ID: "))
        model = input("Enter Car Model: ")
        company = input("Enter company: ")
        price = float(input("Enter Price: "))
        cars.append(Car(vehicle_id, model, company, price, True, "Car"))
    elif choice == 2:
        vehicle_id = int(input("Enter Vehicle ID: "))
        model = input("Enter Car Model: ")
        company = input("Enter company: ")
        price = float(input("Enter Price: "))
        bikes.append(Bike(vehicle_id, model, company, price, True, "Bike"))
    elif choice == 0:
        print("Returning...")
        return
    else:
        print("Please Enter A Valid Option")


def show_vehicles():
    print("[-- CAR LIST --]")
    for car in cars:
        car.display()
    print("----------------")
    print("[-- BIKE LIST --]")
    for bike in bikes:
        bike.display()
    print("-----------------")


def remove_vehicle():
    id_find = int(input("Enter Vehicle ID: "))
    for car in cars:
        if id_find == car.vehicle_id():
            cars.remove(car)
            print(f"Car with the ID {id_find} is successfully removed.")
    for bike in bikes:
        if id_find == bike.vehicle_id():
            cars.remove(bike)
            print(f"Bike with the ID {id_find} is successfully removed.")


def update_status():
    id_find = int(input("Enter The Vehicle ID: "))
    for car in cars:
        if id_find == car.vehicle_id():
            new_status = int(input("Enter status (1/0): "))
            if new_status == 1:
                car.set_status(True)
            elif new_status == 0:
                car.set_status(False)
            else:
                print("Please Enter A valid Option")

    for bike in bikes:
        if id_find == bike.vehicle_id():
            new_status = int(input("Enter status (1/0): "))
            if new_status == 1:
                bike.set_staus(True)
            elif new_status == 0:
                bike.set_status(False)
            else:
                print("Please Enter A valid Option")


def view_my_bookings():
    customer_id = int(input("Enter Your Customer ID: "))
    found = False
    for b in booking:
        if b[0] == customer_id:
            print(f"Booked Vehicle ID: {b[1]}")
            found = True
    if not found:
        print("No bookings found for this customer.")


def view_all_bookings():
    if len(booking) == 0:
        print("No bookings Yet")
    else:
        for b in booking:
            print(f"Customer ID: {b[0]}, Vehicle ID: {b[1]}")


def save_data():
    try:
        with open("cars.json", "w") as f:
            json.dump([car.to_dict() for car in cars], f)
        with open("bikes.json", "w") as f:
            json.dump([bike.to_dict() for bike in bikes], f)
        with open("customer.json", "w") as f:
            json.dump([cust.to_dict() for cust in customer], f)
        with open("staff.json", "w") as f:
            json.dump([stf.to_dict() for stf in staff], f)
        with open("booking.json", "w") as f:
            json.dump(booking, f)
        print("Data saved successfully.")
    except Exception as e:
        print("Error saving data:", e)


def load_data():
    global cars, bikes, customer, staff, booking
    try:
        with open("cars.json", "r") as f:
            cars_data = json.load(f)
            cars = [Car.from_dict(data) for data in cars_data]
        with open("bikes.json", "r") as f:
            bikes_data = json.load(f)
            bikes = [Bike.from_dict(data) for data in bikes_data]
        with open("customer.json", "r") as f:
            customer_data = json.load(f)
            customer = [Customer.from_dict(data) for data in customer_data]
        with open("staff.json", "r") as f:
            staff_data = json.load(f)
            staff = [Staff.from_dict(data) for data in staff_data]
        with open("booking.json", "r") as f:
            booking = json.load(f)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print("Data files not found. Starting with empty data.")
    except Exception as e:
        print("Error loading data:", e)


# TODO: MAKE THE MAIN MENY AND MAKE THE CLASS ATTRIBUTES PRIVATE TO EXERCISE ENCAPSULATION AND MAKE FURTHER ARRAYS
def main():
    load_data()
    running = True
    while running:
        welcome_menu()
        choice = int(input("Enter A choice: "))
        if choice == 1:
            running_1 = True
            while running_1:
                customer_menu()
                choice_1 = int(input("Enter your choice: "))
                if choice_1 == 1:  # View Available Vehicles
                    available_vehicles()
                elif choice_1 == 2:  # Book a Vehicles
                    book_vehicle()
                elif choice_1 == 3:  # Return a Vehicle
                    return_vehicle()
                elif choice_1 == 4:  # My Booking History
                    view_my_bookings()
                elif choice_1 == 0:
                    print("Going Back...")
                    running_1 = False
                else:
                    print("Please Enter A Valid Choice.")

        elif choice == 2:
            running_2 = True
            while running_2:
                staff_menu()
                choice_2 = int(input("Enter your choice: "))
                if choice_2 == 1:  # Add Vehicle to Inventory
                    add_vehicle()
                elif choice_2 == 2:  # View All Vehicle
                    show_vehicles()
                elif choice_2 == 3:  # Update Vehicle Status
                    update_status()
                elif choice_2 == 4:  # Remove Vehicle From inventory
                    remove_vehicle()
                elif choice_2 == 5:  # View Booking History
                    view_all_bookings()
                elif choice_2 == 0:
                    print("Going Back...")
                    running_2 = False
                else:
                    print("Please Enter A valid choice")
        elif choice == 3:
            add_customers()
        elif choice == 4:
            add_staff()
        elif choice == 0:
            save = input("Do you want to save data before exiting? (y/n): ").lower()
            if save == "y":
                save_data()
            print("Thanks for Using the Car Management System")
            running = False
        else:
            print("Please Enter A valid choice.")


if __name__ == '__main__':
    main()
