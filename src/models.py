from typing import List
from enum import Enum


class Schedule:
    def __init__(self, phys_warehouse, polygon, company, courier_id: str, courier_status, vehicle_type, vehicle_volume, vehicle_model, schedule,
                 schedule_status, load_up_window, load_up_status):
        self.phys_warehouse = phys_warehouse
        self.polygon = polygon
        self.company = company
        self.courier_id = str(int(courier_id))
        self.courier_status = courier_status
        self.vehicle_type = vehicle_type
        self.vehicle_volume = vehicle_volume
        self.vehicle_model = vehicle_model
        self.schedule = schedule
        self.schedule_status = schedule_status
        self.load_up_window = load_up_window
        self.load_up_status = load_up_status


class LogisticRequest:
    def __init__(self, date, private_id, public_id: str, orders, courier_name, courier_id: str, courier_company, shift_id,
                 shift_time, expected_time, task_type, request_type, duration, end_time, status, reason, source,
                 payment_type, sum_amount, address, spot_en_route, warehouse, phys_warehouse, polygon, reassign_comment,
                 is_reassigned, new_courier_id):
        self.date = date
        self.private_id = private_id
        self.public_id = public_id
        self.orders = orders
        self.courier_name = courier_name
        self.courier_id = str(int(courier_id))
        self.courier_company = courier_company
        self.shift_id = shift_id
        self.shift_time = shift_time
        self.expected_time = expected_time
        self.task_type = task_type
        self.request_type = request_type
        self.duration = duration
        self.end_time = end_time
        self.status = status
        self.reason = reason
        self.source = source
        self.payment_type = payment_type
        self.sum_amount = sum_amount
        self.address = address
        self.spot_en_route = spot_en_route
        self.warehouse = warehouse
        self.phys_warehouse = phys_warehouse
        self.polygon = polygon
        self.reassign_comment = reassign_comment
        self.is_reassigned = is_reassigned
        self.new_courier_id = new_courier_id


# Прямой или возвратный
class Direction(Enum):
    DROP_SHIP = 'drop_ship'
    RETURN = 'return'

class Address:
    def __init__(self, address_string: str, direction: Direction, status: str):
        self.address_string = address_string
        self.direction = direction
        self.status = status

class CourierRoute:
    def __init__(self, company: str, courier_name: str, courier_id: int, addresses: List[Address]):
        self.company = company
        self.courier_name = courier_name
        self.courier_id = courier_id
        self.addresses = addresses
