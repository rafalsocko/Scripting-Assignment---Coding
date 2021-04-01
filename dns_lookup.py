import requests

API_KEY = ''
BASE_URL = "https://api.macaddress.io"
ENDPOINT_URL = "/v1"
OUTPUT_TYPE = "json"


def get_query_paramteres():
    return {"output": OUTPUT_TYPE, "search": "44:38:39:ff:ef:57"}


def get_headers():
    return {"X-Authentication-Token": API_KEY}


def main():
    request_response = requests.get(BASE_URL + ENDPOINT_URL, params=get_query_paramteres(), headers=get_headers())
    print(request_response.json())


if __name__ == "__main__":
    main()
