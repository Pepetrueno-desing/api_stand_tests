import configuration
import requests
import data


def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body,
        headers=data.headers
    )


def post_products_kits(products_ids):
    return requests.post(
        configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
        json=products_ids,
        headers=data.headers
    )