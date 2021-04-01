import requests
import sys
API_KEY = ''
BASE_URL = "https://api.macaddress.io"
ENDPOINT_URL = "/v1"
OUTPUT_TYPE = "json"


def get_query_paramteres(dns):
    return {"output": OUTPUT_TYPE, "search": dns}


def get_headers():
    return {"X-Authentication-Token": API_KEY}


def parse_response(response):
    return response["vendorDetails"]["companyName"]


def main(dns):
    request_response = requests.get(BASE_URL + ENDPOINT_URL, params=get_query_paramteres(dns), headers=get_headers())
    print(parse_response(request_response.json())+";"+dns)


if __name__ == "__main__":
    main(sys.argv[1])
