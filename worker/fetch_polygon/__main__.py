import logging
import os
import datetime
from fetch_polygon.fetch_polygon import FetchPolygon
from dotenv import load_dotenv
from timeseries.DbWriter import DbWriter

load_dotenv('.env')

logging.basicConfig(
    format="[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

if __name__ == "__main__": # Manual test run
    logging.info("Running Fetch Polygon")
    api_root = os.getenv("POLYGON_API_ROOT")
    api_key = os.getenv("POLYGON_API_KEY")
    influx_host = os.getenv("INFLUXDB_HOST")
    influx_token = os.getenv("INFLUXDB_TOKEN")
    influx_org = os.getenv("INFLUXDB_ORG")
    influx_bucket = os.getenv("INFLUXDB_BUCKET")
    
    assert api_root
    assert api_key
    assert influx_host
    assert influx_token
    assert influx_org
    assert influx_bucket

    fp = FetchPolygon(api_root, api_key)
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    data = fp.fetch_yesterday_data("X:BTCUSD", yesterday)
    if data is None:
        logging.error("Failed to fetch data")

    db = DbWriter(
        influx_host,
        influx_token,
        influx_org,
        influx_bucket,
    )
    for price in data.results:
        db.writePointRaw(
            measurement="crypto_price",
            tag=data.ticker, 
            location="close_price", 
            timestamp=price.t,
            unit="USD",
            value=float(price.c))
        db.writePointRaw(
            measurement="crypto_price",
            tag=data.ticker, 
            location="highest_price", 
            timestamp=price.t,
            unit="USD",
            value=float(price.h))
        db.writePointRaw(
            measurement="crypto_price",
            tag=data.ticker, 
            location="lowest_price", 
            timestamp=price.t,
            unit="USD",
            value=float(price.l))
