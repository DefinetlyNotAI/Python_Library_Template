import requests


def send_get_request(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
