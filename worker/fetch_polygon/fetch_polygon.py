import http.client
import logging
import json
from types import SimpleNamespace

logging.basicConfig(
    format="[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

class FetchPolygon:
    def __init__(self, api_root, api_key) -> None:
        self.api_root = api_root
        self.api_key = api_key

    def fetch_yesterday_data(self, ticker, date):
        # https://polygon.io/docs/crypto/getting-started
        d = date.strftime('%Y-%m-%d')
        endpoint = f'/v2/aggs/ticker/{ticker}/range/15/minute/{d}/{d}?adjusted=true&sort=asc&limit=5000&apiKey='+self.api_key
        url = self.api_root + endpoint
        # logging.info(f'Fetch data: {url}')
        connection = http.client.HTTPSConnection(self.api_root)
        params = {'adjusted': "true", 'sort': 'asc', 'limit': '5000', 'apiKey': self.api_key}
        connection.request('GET', endpoint)
        response = connection.getresponse()
        result = json.loads(response.read().decode(), object_hook=lambda d: SimpleNamespace(**d))
        # logging.info(result)
        connection.close()
        return result

        

