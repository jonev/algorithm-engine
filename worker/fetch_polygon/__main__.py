import logging
import os
from datetime import datetime, date, timedelta
from fetch_polygon.fetch_polygon import FetchPolygon
from dotenv import load_dotenv
from timeseries.DbWriter import DbWriter
from utils.utils import Payload

load_dotenv('.env')

logging.basicConfig(
    format="[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

def run_polygon(id, job, influx_host, influx_token, influx_org, influx_bucket):
    api_root = os.getenv("POLYGON_API_ROOT")
    api_key = os.getenv("POLYGON_API_KEY")
    assert api_root
    assert api_key # This need to be provided manually
    assert influx_host
    assert influx_token
    assert influx_org
    assert influx_bucket
    logging.info(f"Fetch-polygon.io db info: {influx_host}, {influx_org}, {influx_bucket}")
    fp = FetchPolygon(api_root, api_key)
    db = DbWriter(
        influx_host,
        influx_token,
        influx_org,
        influx_bucket,
    )
    # Hent data
    today = date.today()
    yesterday = today - timedelta(days=1)
    for tag in job.Tags:
        data = fp.fetch_yesterday_data(tag, yesterday)
        if data is None:
            logging.error(f"Failed to fetch data from polygon.io, for: {tag}")
            return

        for price in data.results:
            db.writePointRaw(
                measurement="crypto_price",
                tag=data.ticker.replace(":", "_"), 
                location="close_price", 
                timestamp=price.t,
                unit="USD",
                value=float(price.c))
            db.writePointRaw(
                measurement="crypto_price",
                tag=data.ticker.replace(":", "_"), 
                location="highest_price", 
                timestamp=price.t,
                unit="USD",
                value=float(price.h))
            db.writePointRaw(
                measurement="crypto_price",
                tag=data.ticker.replace(":", "_"), 
                location="lowest_price", 
                timestamp=price.t,
                unit="USD",
                value=float(price.l))
        logging.info(f"Fetched and save data from polygon.io, for: {tag}")
    logging.info(f"Fetch-polygon ran with success, on worker: {id}")

if __name__ == "__main__": # Manual test run
    logging.info("Running Fetch Polygon manually")
    run_polygon("manual", Payload('{"Tags": ["X:BTCUSD"]}'), "http://influxdb:8086", "my-super-secret-auth-token", "dev", "test_bucket")