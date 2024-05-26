import requests
import configuration
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)


def get_created_order_track_number(response):
    return response.json()["track"]


def get_order_track(track_number):
    order_track_number_body = get_order_track_number_body(track_number)
    response = requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                            json=order_track_number_body)
    return response



def get_order_track_number_body(track_number):
    current_body = data.get_order_track.copy()
    current_body["t"] = track_number
    return current_body