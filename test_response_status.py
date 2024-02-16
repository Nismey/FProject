import setup_order
import data

def test_status_of_order_is_200():

    order = setup_order.post_new_order(data.order_body_full) # 1 шаг - запрос на создание заказа
    track = order.json()['track'] # 2 шаг - сохранение номера трека заказа
    setup_order.getting_order_data(track) # 3 шаг - выполняем запрос на получение заказа по треку заказа
    sp = {'t': track}
    response = setup_order.getting_order_data(sp['t'])
    assert response == 200 #Проверяем код ответа 200

# Медведева Дарья 13 когорта Финальный проект. Инженер по тестированию плюс