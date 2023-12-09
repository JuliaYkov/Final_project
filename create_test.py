# Юлия Яковлева, 11-я когорта - Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data




def positive_assert():
    numbers_response = sender_stand_request.post_new_order(data.order_body)
    data.track_number["t"] = numbers_response.json()['track']
    orders_respons = sender_stand_request.get_receiving_an_orders()
    assert orders_respons.status_code == 200


def test_receiving_an_orders():
    positive_assert()

