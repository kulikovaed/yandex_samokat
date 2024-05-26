import data
import sender_stand_request


def test_create_order_and_get_order_by_number():
    # step 1 - create order
    order_response = sender_stand_request.post_new_order(data.post_order_body)

    # step 2 - save created order number
    order_track_number = sender_stand_request.get_created_order_track_number(order_response)

    # step 3 - get order by order number
    created_order_response = sender_stand_request.get_order_track(order_track_number)

    # step 4 - check positive response code
    assert created_order_response.status_code == 200