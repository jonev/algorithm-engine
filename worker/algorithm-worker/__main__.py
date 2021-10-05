from datetime import datetime
import logging
import uuid
import json
import os
from .queue_service import QueueService
from dotenv import load_dotenv

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
    
    logging.error(f"Algorithm type not supported: {job.Algorithm}")



if __name__ == "__main__":
    url = os.getenv("RABBITMQ_URL")
    assert url
    logging.info(f"Worker starting {datetime.now()}, with id: {id}, rabbitmq-url: {url.split('@')[1]}")
    q = QueueService(url)
    assert q
    q.listen(on_message)
