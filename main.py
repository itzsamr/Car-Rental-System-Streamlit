from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from exception.myexceptions import *
from pyodbc import *
from tabulate import tabulate
from datetime import datetime


class CarRentalSystem:
    @staticmethod
    def start():
        car_lease_repository = ICarLeaseRepositoryImpl()

        while True:
            print("\n=====|Main Menu:|=====")
            print("1. Customer Management")
            print("2. Vehicle Management")
            print("3. Lease Management")
            print("4. Payment Handling")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                CarRentalSystem.customer_management(car_lease_repository)

            elif choice == "2":
                CarRentalSystem.vehicle_management(car_lease_repository)

            elif choice == "3":
                CarRentalSystem.lease_management(car_lease_repository)

            elif choice == "4":
                CarRentalSystem.payment_handling(car_lease_repository)

            elif choice == "5":
                print("Exiting program.")
                break

            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def customer_management(car_lease_repository):
        while True:
            print("\n=====|Customer Management:|=====")
            print("1. Add Customer")
            print("2. Remove Customer")
            print("3. List Customers")
            print("4. Find Customer by ID")
            print("5. Back to Main Menu")

            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                CarRentalSystem.add_customer(car_lease_repository)

            elif sub_choice == "2":
                CarRentalSystem.remove_customer(car_lease_repository)

            elif sub_choice == "3":
                CarRentalSystem.list_customers(car_lease_repository)

            elif sub_choice == "4":
                CarRentalSystem.find_customer_by_id(car_lease_repository)

            elif sub_choice == "5":
                break

            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def add_customer(car_lease_repository):
        try:
            customer_id = input("Enter new customer ID: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            car_lease_repository.add_customer(
                customer_id, first_name, last_name, email, phone_number
            )
            print("Customer added successfully.")
        except Exception as e:
            print(f"Error adding customer: {e}")

    @staticmethod
    def remove_customer(car_lease_repository):
        try:
            customer_id = int(input("Enter customer ID to remove: "))
            car_lease_repository.remove_customer(customer_id)
            print("Customer removed successfully.")
        except Exception as e:
            print(f"Error removing customer: {e}")

    @staticmethod
    def list_customers(car_lease_repository):
        try:
            customers = car_lease_repository.list_customers()
            if customers:
                headers = customers[0].keys()
                rows = [customer.values() for customer in customers]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print("No customers found.")
        except Exception as e:
            print(f"Error listing customers: {e}")

    @staticmethod
    def find_customer_by_id(car_lease_repository):
        try:
            customer_id = input("Enter customer ID to find: ")
            customer = car_lease_repository.find_customer_by_id(customer_id)
            if customer:
                headers = [
                    "Customer ID",
                    "First Name",
                    "Last Name",
                    "Email",
                    "Phone Number",
                ]
                table = [
                    [
                        customer["customerID"],
                        customer["firstName"],
                        customer["lastName"],
                        customer["email"],
                        customer["phoneNumber"],
                    ]
                ]
                print(tabulate(table, headers=headers, tablefmt="grid"))
            else:
                print("Customer not found.")
        except CustomerNotFoundException as e:
            print(f"Error: {e}")

    @staticmethod
    def vehicle_management(car_lease_repository):
        while True:
            print("\n=====|Vehicle Management:|=====")
            print("1. Add Vehicle")
            print("2. Remove Vehicle")
            print("3. List Available Cars")
            print("4. List Rented Cars")
            print("5. Find Car by ID")
            print("6. Back to Main Menu")

            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                CarRentalSystem.add_car(car_lease_repository)

            elif sub_choice == "2":
                CarRentalSystem.remove_car(car_lease_repository)

            elif sub_choice == "3":
                CarRentalSystem.list_available_cars(car_lease_repository)

            elif sub_choice == "4":
                CarRentalSystem.list_of_rented_cars(car_lease_repository)

            elif sub_choice == "5":
                CarRentalSystem.find_car_by_id(car_lease_repository)

            elif sub_choice == "6":
                break

            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def add_car(car_lease_repository):
        try:
            vehicle_id = input("Enter vehicle ID: ")
            make = input("Enter make: ")
            model = input("Enter model: ")
            year = int(input("Enter year: "))
            daily_rate = float(input("Enter daily rate: "))
            status = input("Enter status (available/notAvailable): ")
            passenger_capacity = int(input("Enter passenger capacity: "))
            engine_capacity = float(input("Enter engine capacity: "))
            car_lease_repository.add_car(
                vehicle_id,
                make,
                model,
                year,
                daily_rate,
                status,
                passenger_capacity,
                engine_capacity,
            )
            print("Vehicle added successfully.")
        except Exception as e:
            print(f"Error adding vehicle: {e}")

    @staticmethod
    def remove_car(car_lease_repository):
        try:
            vehicle_id = input("Enter vehicle ID to remove: ")
            car_lease_repository.remove_car(vehicle_id)
        except Exception as e:
            print(f"Error removing vehicle: {e}")

    @staticmethod
    def list_available_cars(car_lease_repository):
        try:
            cars = car_lease_repository.list_available_cars()
            if cars:
                headers = cars[0].keys()
                rows = [list(car.values()) for car in cars]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print("No available cars found.")
        except Exception as e:
            print(f"Error listing available cars: {e}")

    @staticmethod
    def list_of_rented_cars(car_lease_repository):
        try:
            cars = car_lease_repository.list_of_rented_cars()
            if cars:
                headers = cars[0].keys()
                rows = [list(car.values()) for car in cars]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print("No available cars found.")
        except Exception as e:
            print(f"Error listing available cars: {e}")

    @staticmethod
    def find_car_by_id(car_lease_repository):
        try:
            car_id = input("Enter car ID to find: ")
            car = car_lease_repository.find_car_by_id(car_id)
            if car:
                headers = [
                    "Car ID",
                    "Make",
                    "Model",
                    "Year",
                    "Daily Rate",
                    "Status",
                    "Passenger Capacity",
                    "Engine Capacity",
                ]
                table = [
                    [
                        car["carID"],
                        car["make"],
                        car["model"],
                        car["year"],
                        car["dailyRate"],
                        car["status"],
                        car["passengerCapacity"],
                        car["engineCapacity"],
                    ]
                ]
                print(tabulate(table, headers=headers, tablefmt="grid"))
            else:
                print("Car not found.")
        except VehicleNotFoundException as e:
            print(f"Error: {e}")

    @staticmethod
    def lease_management(car_lease_repository):
        while True:
            print("\n=====|Lease Management:|=====")
            print("1. Create Lease")
            print("2. Return Car")
            print("3. List Active Leases")
            print("4. List Lease History")
            print("5. Back to Main Menu")

            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                CarRentalSystem.create_lease(car_lease_repository)

            elif sub_choice == "2":
                CarRentalSystem.return_car(car_lease_repository)

            elif sub_choice == "3":
                CarRentalSystem.list_active_leases(car_lease_repository)

            elif sub_choice == "4":
                CarRentalSystem.list_lease_history(car_lease_repository)

            elif sub_choice == "5":
                break

            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def create_lease(car_lease_repository):
        try:
            lease_id = input("Enter new lease ID: ")
            customer_id = input("Enter customer ID: ")
            car_id = input("Enter car ID: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            lease_type = input("Enter lease type (DailyLease/MonthlyLease): ")
            car_lease_repository.create_lease(
                lease_id, customer_id, car_id, start_date, end_date, lease_type
            )
        except Exception as e:
            print(f"Error creating lease: {e}")

    @staticmethod
    def return_car(car_lease_repository):
        try:
            lease_id = input("Enter lease ID to return the car: ")
            car_lease_repository.return_car(lease_id)
        except Exception as e:
            print(f"Error returning car: {e}")

    @staticmethod
    def list_active_leases(car_lease_repository):
        try:
            leases = car_lease_repository.list_active_leases()
            if leases:
                headers = [
                    "Lease ID",
                    "Vehicle ID",
                    "Customer ID",
                    "Start Date",
                    "End Date",
                    "Lease Type",
                ]
                rows = [
                    [
                        lease["leaseID"],
                        lease["vehicleID"],
                        lease["customerID"],
                        lease["startDate"],
                        lease["endDate"],
                        lease["type"],
                    ]
                    for lease in leases
                ]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print("No active leases found.")
        except Exception as e:
            print(f"Error listing active leases: {e}")

    @staticmethod
    def list_lease_history(car_lease_repository):
        try:
            leases = car_lease_repository.list_lease_history()
            if leases:
                headers = [
                    "Lease ID",
                    "Vehicle ID",
                    "Customer ID",
                    "Start Date",
                    "End Date",
                    "Lease Type",
                ]
                rows = [
                    [
                        lease["leaseID"],
                        lease["vehicleID"],
                        lease["customerID"],
                        lease["startDate"],
                        lease["endDate"],
                        lease["type"],
                    ]
                    for lease in leases
                ]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print("No lease history found.")
        except Exception as e:
            print(f"Error listing lease history: {e}")

    @staticmethod
    def payment_handling(car_lease_repository):
        while True:
            print("\n=====|Payment Handling:|=====")
            print("1. Record Payment")
            print("2. Retrieve Payment History")
            print("3. Calculate Total Revenue")
            print("4. List All Payments")
            print("5. Back to Main Menu")

            sub_choice = input("Enter your choice: ")

            if sub_choice == "1":
                CarRentalSystem.record_payment(car_lease_repository)

            elif sub_choice == "2":
                CarRentalSystem.retrieve_payment_history(car_lease_repository)

            elif sub_choice == "3":
                CarRentalSystem.calculate_total_revenue(car_lease_repository)

            elif sub_choice == "4":
                CarRentalSystem.list_all_payments(car_lease_repository)

            elif sub_choice == "5":
                break

            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def record_payment(car_lease_repository):
        try:
            payment_id = int(input("Enter new payment ID: "))
            lease_id = int(input("Enter lease ID: "))
            payment_date = datetime.strptime(
                input("Enter payment date (YYYY-MM-DD): "), "%Y-%m-%d"
            )
            amount = float(input("Enter payment amount: "))
            car_lease_repository.record_payment(
                payment_id, lease_id, payment_date, amount
            )
            print("Payment recorded successfully.")
        except ValueError:
            print(
                "Invalid input. Please enter valid lease ID, payment date, and payment amount."
            )
        except Exception as e:
            print(f"Error recording payment: {e}")

    @staticmethod
    def retrieve_payment_history(car_lease_repository):
        try:
            lease_id = int(input("Enter lease ID: "))
            payments = car_lease_repository.retrieve_payment_history(lease_id)
            if payments:
                headers = ["Lease ID", "Payment ID", "Payment Date", "Amount"]
                rows = [
                    [
                        payment["leaseID"],
                        payment["paymentID"],
                        payment["paymentDate"],
                        payment["amount"],
                    ]
                    for payment in payments
                ]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print("No payment history found for the given lease ID.")
        except ValueError:
            print("Invalid input. Please enter a valid lease ID.")
        except Exception as e:
            print(f"Error retrieving payment history: {e}")

    @staticmethod
    def calculate_total_revenue(car_lease_repository):
        try:
            total_revenue = car_lease_repository.calculate_total_revenue()
            print(tabulate([[f"Total Revenue: {total_revenue}"]], tablefmt="grid"))
        except Exception as e:
            print(f"Error calculating total revenue: {e}")

    @staticmethod
    def list_all_payments(car_lease_repository):
        try:
            payments = car_lease_repository.list_all_payments()
            if payments:
                headers = payments[0].keys()
                rows = [payment.values() for payment in payments]
                print(tabulate(rows, headers=headers, tablefmt="grid"))
            else:
                print("No payments found.")
        except Exception as e:
            print(f"Error listing all payments: {e}")


if __name__ == "__main__":
    CarRentalSystem.start()
