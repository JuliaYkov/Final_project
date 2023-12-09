import configuration
import requests
import data


# Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body)


# Сохранение номера заказа
response = post_new_order(data.order_body)
data.track_number["t"] = response.json()['track']


# Получение заказа по его номеру
def get_receiving_an_orders():
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_RECEIVING_AN_ORDERS,
                         params={'t': data.track_number["t"]})

