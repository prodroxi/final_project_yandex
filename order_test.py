import configuration
import sender_stand_request
import data

def test_create_and_get_order():
    # Шаг 1: создаём заказ
    create_response = sender_stand_request.post_new_order(data.order_body)
    
    # Проверяем, что заказ создан успешно
    assert create_response.status_code == 201, \
        f"Ожидался статус 201, получен {create_response.status_code}"
    
    # Шаг 2: сохраняем номер трека
    response_body = create_response.json()
    track = response_body.get("track")
    assert track is not None, "Трек заказа не получен в ответе"
    print(f"Создан заказ с треком: {track}")
    
    # Шаг 3: получаем заказ по треку
    get_response = sender_stand_request.get_order_by_track(track)
    
    # Шаг 4: проверяем, что код ответа равен 200
    assert get_response.status_code == 200, \
        f"Ожидался статус 200, получен {get_response.status_code}"
    
    # Дополнительная проверка: трек в ответе совпадает
    order_data = get_response.json()
    assert order_data["order"]["track"] == track, \
        "Трек в полученном заказе не совпадает с созданным"
    
    print(f"Заказ успешно получен! Статус ответа: {get_response.status_code}")