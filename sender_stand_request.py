import requests
import configuration
import data

def post_new_order(body):
    """Создание нового заказа"""
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        headers={"Content-Type": "application/json"}
    )

def get_order_by_track(track):
    """Получение заказа по номеру трека"""
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
        params={"t": track}
    )