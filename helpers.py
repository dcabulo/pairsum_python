import requests

NBA_ENDPOINT = "https://mach-eight.uc.r.appspot.com/"


def fetch_data():
    response = requests.get(NBA_ENDPOINT)
    response.raise_for_status()
    return response.json().get("values")

