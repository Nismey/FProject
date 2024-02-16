import config
import data
import requests


def post_new_order(order_body):  # функция POST-запроса на создание заказа
    track = requests.post(config.URL + config.ORDER_CREATE_PATH, json=order_body)
    return track


def getting_order_data(track):
    response = requests.get(config.URL + config.GET_ORDER_DATA_PATH + '?t=' + str(track))
    return response.status_code


post_new_order(data.order_body_full)