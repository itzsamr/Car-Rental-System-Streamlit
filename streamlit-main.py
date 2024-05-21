import streamlit as st
from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from exception.myexceptions import *
from pyodbc import *
from tabulate import tabulate
from datetime import datetime


class CarRentalSystem:
    def __init__(self):
        self.car_lease_repository = ICarLeaseRepositoryImpl()

    def main(self):
        st.title("Car Rental System")
        menu = [
            "Customer Management",
            "Vehicle Management",
            "Lease Management",
            "Payment Handling",
            "Exit",
        ]
        choice = st.sidebar.selectbox("Main Menu", menu)

        if choice == "Customer Management":
            self.customer_management()
        elif choice == "Vehicle Management":
            self.vehicle_management()
        elif choice == "Lease Management":
            self.lease_management()
        elif choice == "Payment Handling":
            self.payment_handling()
        elif choice == "Exit":
            st.write("Exiting program.")

    def customer_management(self):
        st.subheader("Customer Management")
        sub_menu = [
            "Add Customer",
            "Remove Customer",
            "List Customers",
            "Find Customer by ID",
        ]
        sub_choice = st.selectbox("Options", sub_menu)

        if sub_choice == "Add Customer":
            self.add_customer()
        elif sub_choice == "Remove Customer":
            self.remove_customer()
        elif sub_choice == "List Customers":
            self.list_customers()
        elif sub_choice == "Find Customer by ID":
            self.find_customer_by_id()

    def add_customer(self):
        st.subheader("Add Customer")
        customer_id = st.text_input("Enter new customer ID:")
        first_name = st.text_input("Enter first name:")
        last_name = st.text_input("Enter last name:")
        email = st.text_input("Enter email:")
        phone_number = st.text_input("Enter phone number:")

        if st.button("Add Customer"):
            try:
                self.car_lease_repository.add_customer(
                    customer_id, first_name, last_name, email, phone_number
                )
                st.success("Customer added successfully.")
            except Exception as e:
                st.error(f"Error adding customer: {e}")

    def remove_customer(self):
        st.subheader("Remove Customer")
        customer_id = st.text_input("Enter customer ID to remove:")

        if st.button("Remove Customer"):
            try:
                self.car_lease_repository.remove_customer(customer_id)
                st.success("Customer removed successfully.")
            except Exception as e:
                st.error(f"Error removing customer: {e}")

    def list_customers(self):
        st.subheader("List Customers")
        try:
            customers = self.car_lease_repository.list_customers()
            if customers:
                st.write(customers)
            else:
                st.info("No customers found.")
        except Exception as e:
            st.error(f"Error listing customers: {e}")

    def find_customer_by_id(self):
        st.subheader("Find Customer by ID")
        customer_id = st.text_input("Enter customer ID to find:")

        if st.button("Find Customer"):
            try:
                customer = self.car_lease_repository.find_customer_by_id(customer_id)
                if customer:
                    st.write(customer)
                else:
                    st.info("Customer not found.")
            except CustomerNotFoundException as e:
                st.error(f"Error: {e}")

    def vehicle_management(self):
        st.subheader("Vehicle Management")
        sub_menu = [
            "Add Vehicle",
            "Remove Vehicle",
            "List Available Cars",
            "List Rented Cars",
            "Find Car by ID",
        ]
        sub_choice = st.selectbox("Options", sub_menu)

        if sub_choice == "Add Vehicle":
            self.add_car()
        elif sub_choice == "Remove Vehicle":
            self.remove_car()
        elif sub_choice == "List Available Cars":
            self.list_available_cars()
        elif sub_choice == "List Rented Cars":
            self.list_of_rented_cars()
        elif sub_choice == "Find Car by ID":
            self.find_car_by_id()

    def add_car(self):
        st.subheader("Add Vehicle")
        vehicle_id = st.text_input("Enter vehicle ID:")
        make = st.text_input("Enter make:")
        model = st.text_input("Enter model:")
        year = st.number_input(
            "Enter year:", min_value=1900, max_value=datetime.now().year
        )
        daily_rate = st.number_input("Enter daily rate:")
        status = st.selectbox("Enter status:", ["available", "notAvailable"])
        passenger_capacity = st.number_input("Enter passenger capacity:", min_value=1)
        engine_capacity = st.number_input("Enter engine capacity:")

        if st.button("Add Vehicle"):
            try:
                self.car_lease_repository.add_car(
                    vehicle_id,
                    make,
                    model,
                    year,
                    daily_rate,
                    status,
                    passenger_capacity,
                    engine_capacity,
                )
                st.success("Vehicle added successfully.")
            except Exception as e:
                st.error(f"Error adding vehicle: {e}")

    def remove_car(self):
        st.subheader("Remove Vehicle")
        vehicle_id = st.text_input("Enter vehicle ID to remove:")

        if st.button("Remove Vehicle"):
            try:
                self.car_lease_repository.remove_car(vehicle_id)
                st.success("Vehicle removed successfully.")
            except Exception as e:
                st.error(f"Error removing vehicle: {e}")

    def list_available_cars(self):
        st.subheader("List Available Cars")
        try:
            cars = self.car_lease_repository.list_available_cars()
            if cars:
                st.write(cars)
            else:
                st.info("No available cars found.")
        except Exception as e:
            st.error(f"Error listing available cars: {e}")

    def list_of_rented_cars(self):
        st.subheader("List Rented Cars")
        try:
            cars = self.car_lease_repository.list_of_rented_cars()
            if cars:
                st.write(cars)
            else:
                st.info("No rented cars found.")
        except Exception as e:
            st.error(f"Error listing rented cars: {e}")

    def find_car_by_id(self):
        st.subheader("Find Car by ID")
        car_id = st.text_input("Enter car ID to find:")

        if st.button("Find Car"):
            try:
                car = self.car_lease_repository.find_car_by_id(car_id)
                if car:
                    st.write(car)
                else:
                    st.info("Car not found.")
            except VehicleNotFoundException as e:
                st.error(f"Error: {e}")

    def lease_management(self):
        st.subheader("Lease Management")
        sub_menu = [
            "Create Lease",
            "Return Car",
            "List Active Leases",
            "List Lease History",
        ]
        sub_choice = st.selectbox("Options", sub_menu)

        if sub_choice == "Create Lease":
            self.create_lease()
        elif sub_choice == "Return Car":
            self.return_car()
        elif sub_choice == "List Active Leases":
            self.list_active_leases()
        elif sub_choice == "List Lease History":
            self.list_lease_history()

    def create_lease(self):
        st.subheader("Create Lease")
        lease_id = st.text_input("Enter new lease ID:")
        customer_id = st.text_input("Enter customer ID:")
        car_id = st.text_input("Enter car ID:")
        start_date = st.date_input("Enter start date:")
        end_date = st.date_input("Enter end date:")
        lease_type = st.selectbox("Enter lease type:", ["DailyLease", "MonthlyLease"])

        if st.button("Create Lease"):
            try:
                self.car_lease_repository.create_lease(
                    lease_id, customer_id, car_id, start_date, end_date, lease_type
                )
                st.success("Lease created successfully.")
            except Exception as e:
                st.error(f"Error creating lease: {e}")

    def return_car(self):
        st.subheader("Return Car")
        lease_id = st.text_input("Enter lease ID to return the car:")

        if st.button("Return Car"):
            try:
                self.car_lease_repository.return_car(lease_id)
                st.success("Car returned successfully.")
            except Exception as e:
                st.error(f"Error returning car: {e}")

    def list_active_leases(self):
        st.subheader("List Active Leases")
        try:
            leases = self.car_lease_repository.list_active_leases()
            if leases:
                st.write(leases)
            else:
                st.info("No active leases found.")
        except Exception as e:
            st.error(f"Error listing active leases: {e}")

    def list_lease_history(self):
        st.subheader("List Lease History")
        try:
            leases = self.car_lease_repository.list_lease_history()
            if leases:
                st.write(leases)
            else:
                st.info("No lease history found.")
        except Exception as e:
            st.error(f"Error listing lease history: {e}")

    def payment_handling(self):
        st.subheader("Payment Handling")
        sub_menu = [
            "Record Payment",
            "Retrieve Payment History",
            "Calculate Total Revenue",
            "List All Payments",
        ]
        sub_choice = st.selectbox("Options", sub_menu)

        if sub_choice == "Record Payment":
            self.record_payment()
        elif sub_choice == "Retrieve Payment History":
            self.retrieve_payment_history()
        elif sub_choice == "Calculate Total Revenue":
            self.calculate_total_revenue()
        elif sub_choice == "List All Payments":
            self.list_all_payments()

    def record_payment(self):
        st.subheader("Record Payment")
        payment_id = st.text_input("Enter new payment ID:")
        lease_id = st.text_input("Enter lease ID:")
        payment_date = st.date_input("Enter payment date:")
        amount = st.number_input("Enter payment amount:")

        if st.button("Record Payment"):
            try:
                self.car_lease_repository.record_payment(
                    payment_id, lease_id, payment_date, amount
                )
                st.success("Payment recorded successfully.")
            except ValueError:
                st.error(
                    "Invalid input. Please enter valid lease ID, payment date, and payment amount."
                )
            except Exception as e:
                st.error(f"Error recording payment: {e}")

    def retrieve_payment_history(self):
        st.subheader("Retrieve Payment History")
        lease_id = st.text_input("Enter lease ID:")

        if st.button("Retrieve Payment History"):
            try:
                payments = self.car_lease_repository.retrieve_payment_history(lease_id)
                if payments:
                    st.write(payments)
                else:
                    st.info("No payment history found for the given lease ID.")
            except ValueError:
                st.error("Invalid input. Please enter a valid lease ID.")
            except Exception as e:
                st.error(f"Error retrieving payment history: {e}")

    def calculate_total_revenue(self):
        st.subheader("Calculate Total Revenue")
        if st.button("Calculate"):
            try:
                total_revenue = self.car_lease_repository.calculate_total_revenue()
                st.write(f"Total Revenue: {total_revenue}")
            except Exception as e:
                st.error(f"Error calculating total revenue: {e}")

    def list_all_payments(self):
        st.subheader("List All Payments")
        try:
            payments = self.car_lease_repository.list_all_payments()
            if payments:
                st.write(payments)
            else:
                st.info("No payments found.")
        except Exception as e:
            st.error(f"Error listing all payments: {e}")


if __name__ == "__main__":
    car_rental_system = CarRentalSystem()
    car_rental_system.main()
