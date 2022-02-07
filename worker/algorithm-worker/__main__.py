from datetime import datetime, date, timedelta
import logging
import uuid
import os

from fetch_polygon.__main__ import run_polygon
from utils.utils import Payload
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
id = uuid.uuid4() # Id of the worker instance running this code. To be able to differentiate the different workers.


# This is trigged by an incoming job
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
            influx_host = os.getenv("INFLUXDB_HOST")
            influx_token = os.getenv("INFLUXDB_TOKEN")
            influx_org = os.getenv("INFLUXDB_ORG")
            influx_bucket = os.getenv("INFLUXDB_BUCKET")
            run_polygon(id, job, influx_host, influx_token, influx_org, influx_bucket)
            return
        
        logging.error(f"Algorithm type not supported: {job.Algorithm}")
    except:
        logging.exception(f"Error occurred in worker")



if __name__ == "__main__": # This is running in production
    url = os.getenv("RABBITMQ_URL")
    assert url
    logging.info(f"Worker starting {datetime.now()}, with id: {id}, rabbitmq-url: {url.split('@')[1]}")
    q = QueueService(url)
    assert q
    q.listen(on_message)
