from datetime import datetime, date, timedelta
import logging
import uuid
import json
import os
from .queue_service import QueueService
from dotenv import load_dotenv
from fetch_polygon.fetch_polygon import FetchPolygon
from timeseries.DbWriter import DbWriter

load_dotenv('.env')

logging.basicConfig(
    format="[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)
id = uuid.uuid4()

class Payload(object):
     def __init__(self, j):
         self.__dict__ = json.loads(j)

def on_message(body):
    try:
        job = Payload(body)
        logging.info(f"Worker: {id}, incoming job: {job.Id}, customer: {job.Customer} algorithm: {job.Algorithm}, start: {job.Start}, end: {job.End}, tags: {job.Tags}")
        if job.Algorithm == "Test-algo":
            logging.info(f"Worker: {id}, Test-algo done")
            return
        
        if job.Algorithm == "rnn":
            logging.info(f"Worker: {id}, RNN")
            # Koble til DB
            # Hent data
            # Gjør prediction
            # Avgjør om det er en alarm
            # Skriv rapport om det er alarm
            return

        if job.Algorithm == "Fetch-polygon.io":
            logging.info(f"Worker: {id}, Fetch-polygon.io, tags: {job.Tags}")
            # Setup
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
                data = fp.fetch_yesterday_data(tag[0], yesterday)
                # data = fp.fetch_yesterday_data("X:BTCUSD", yesterday)
                # Skriv data til databasen
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
            logging.info(f"Fetch-polygon ran with success, on worker: {id}")
            return
        
        logging.error(f"Algorithm type not supported: {job.Algorithm}")
    except:
        logging.exception(f"Error occurred in worker")



if __name__ == "__main__":
    url = os.getenv("RABBITMQ_URL")
    assert url
    logging.info(f"Worker starting {datetime.now()}, with id: {id}, rabbitmq-url: {url.split('@')[1]}")
    q = QueueService(url)
    assert q
    q.listen(on_message)
