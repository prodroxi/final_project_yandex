import configuration
import sender_stand_request
import data
# Шумилов Станислав, 40-я когорта — Финальный проект. Инженер по тестированию плюс

def test_create_order_success():
    create_response = sender_stand_request.post_new_order(data.order_body)
    assert create_response.status_code == 201

def test_create_order_returns_track():
    create_response = sender_stand_request.post_new_order(data.order_body)
    response_body = create_response.json()
    assert "track" in response_body
    assert response_body["track"] is not None

def test_get_order_by_track_success():
    create_response = sender_stand_request.post_new_order(data.order_body)
    track = create_response.json()["track"]
    
    get_response = sender_stand_request.get_order_by_track(track)
    assert get_response.status_code == 200
