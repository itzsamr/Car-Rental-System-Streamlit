import unittest
from dao.ICarLeaseRepositoryImpl import ICarLeaseRepositoryImpl
from datetime import datetime
from exception.myexceptions import *


class TestCarCreation(unittest.TestCase):

    def setUp(self):
        self.car_repo = ICarLeaseRepositoryImpl()
        self.lease_repo = ICarLeaseRepositoryImpl()

    def test_add_car(self):

        vehicle_id = 19
        make = "Honda"
        model = "Shine"
        year = 2022
        daily_rate = 50.0
        status = "available"
        passenger_capacity = 5
        engine_capacity = 2.0

        self.car_repo.add_car(
            vehicle_id,
            make,
            model,
            year,
            daily_rate,
            status,
            passenger_capacity,
            engine_capacity,
        )

        added_car = self.car_repo.find_car_by_id(vehicle_id)

        self.assertEqual(added_car["make"], make)
        self.assertEqual(added_car["model"], model)
        self.assertEqual(added_car["year"], year)
        self.assertEqual(added_car["dailyRate"], daily_rate)
        self.assertEqual(added_car["status"], status)
        self.assertEqual(added_car["passengerCapacity"], passenger_capacity)
        self.assertEqual(added_car["engineCapacity"], engine_capacity)

    def tearDown(self):
        vehicle_id = 19
        self.car_repo.remove_car(vehicle_id)

    def test_create_lease(self):
        lease_id = 72
        customer_id = 1
        car_id = 1
        start_date = datetime.now()
        end_date = datetime.now()
        lease_type = "DailyLease"

        self.lease_repo.create_lease(
            lease_id,
            customer_id,
            car_id,
            start_date,
            end_date,
            lease_type,
        )

        leases = self.lease_repo.list_lease_history()
        created_lease = next(
            (lease for lease in leases if lease["leaseID"] == lease_id), None
        )
        self.assertIsNotNone(created_lease, "Lease should exist in the database.")

    def test_retrieve_lease(self):
        lease_id = 79
        customer_id = 1
        car_id = 1
        start_date = "2023-11-12"
        end_date = "2023-12-29"
        lease_type = "MonthlyLease"

        self.lease_repo.create_lease(
            lease_id,
            customer_id,
            car_id,
            start_date,
            end_date,
            lease_type,
        )

        leases = self.lease_repo.list_lease_history()

        retrieved_lease = next(
            (lease for lease in leases if lease["leaseID"] == lease_id), None
        )

        self.assertIsNotNone(retrieved_lease, "Lease should be retrieved successfully.")
        self.assertEqual(retrieved_lease["leaseID"], lease_id)
        self.assertEqual(retrieved_lease["customerID"], customer_id)
        self.assertEqual(retrieved_lease["vehicleID"], car_id)
        self.assertEqual(retrieved_lease["startDate"], start_date)
        self.assertEqual(retrieved_lease["endDate"], end_date)
        self.assertEqual(retrieved_lease["type"], lease_type)

    def test_vehicle_not_found_exception(self):
        non_existent_vehicle_id = 9999
        with self.assertRaises(VehicleNotFoundException) as context:
            self.lease_repo.find_car_by_id(non_existent_vehicle_id)
        self.assertEqual(
            str(context.exception),
            f"Vehicle with ID {non_existent_vehicle_id} not found in the database",
        )

    def test_lease_not_found_exception(self):
        non_existent_lease_id = 9999
        with self.assertRaises(LeaseNotFoundException) as context:
            self.lease_repo.return_car(non_existent_lease_id)
        self.assertEqual(
            str(context.exception),
            f"Lease with ID {non_existent_lease_id} not found in the database",
        )

    def test_customer_not_found_exception(self):
        non_existent_customer_id = 9999
        with self.assertRaises(CustomerNotFoundException) as context:
            self.lease_repo.find_customer_by_id(non_existent_customer_id)
        self.assertEqual(
            str(context.exception),
            f"Customer with ID {non_existent_customer_id} not found in the database",
        )


if __name__ == "__main__":
    unittest.main()
