class VehicleNotFoundException(Exception):
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def __str__(self):
        return f"Vehicle with ID {self.vehicle_id} not found in the database"


class LeaseNotFoundException(Exception):
    def __init__(self, lease_id):
        self.lease_id = lease_id

    def __str__(self):
        return f"Lease with ID {self.lease_id} not found in the database"


class CustomerNotFoundException(Exception):
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def __str__(self):
        return f"Customer with ID {self.customer_id} not found in the database"
