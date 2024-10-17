from collections import defaultdict
from typing import List
from reader import get_logistic_requests, get_schedules
from models import CourierRoute, Address, LogisticRequest, Direction

drop_ship_vehicle_types = {'Дзер ДО (забор+возвраты) 6', 'Дзер ДО (забор+возвраты)'}
good_order_statuses = {'В процессе', 'Выполнено'}

def get_courier_routes() -> List[CourierRoute]:
    """
    Собирает объекты курьеров и их адресов из расписаний и заказов
    """
    courier_routes = []

    orders_by_courier_id = defaultdict(list)
    for order in get_logistic_requests():
        orders_by_courier_id[order.courier_id].append(order)
    orders_by_courier_id = dict(orders_by_courier_id)

    all_schedules = get_schedules()
    for courier_schedule in  all_schedules:
        # Берем id курьера из смен и получаем заказы по id курьера из мап с заказами
        orders_for_courier = orders_by_courier_id.get(courier_schedule.courier_id)
        # Получаем имя курьера из любого задания
        courier_name = ''
        if orders_for_courier:
            courier_name = orders_for_courier[0].courier_name

        # Возможно, что курьера дропнуло и для него не будет заказов в мапе
        # Значит, что адреса останутся пустыми
        addresses = []
        if orders_for_courier:
            for order in orders_for_courier:
                address = Address(order.address, identify_address_type(order), order.status)
                addresses.append(address)

        courier_route = CourierRoute(courier_schedule.company, courier_name, int(courier_schedule.courier_id), addresses)
        courier_routes.append(courier_route)

    return courier_routes


def identify_address_type(order: LogisticRequest) -> Direction | None:
    """
    Возвращает тип адреса или None, если его не удалось определить
    """
    if not (order.public_id and order.public_id.startswith('TMM') and order.status in good_order_statuses):
        return None

    if order.request_type == 'Дропофф (забор)':
        return Direction.DROP_SHIP

    if order.request_type == 'Дропофф (возврат)':
        return Direction.RETURN

    # Во всех остальных случаях
    return None
