import logging
import os
from datetime import datetime
from rnn.rnn import RNN
from dateutil.relativedelta import relativedelta
from timeseries.DbReader import DbReader

logging.basicConfig(
    format="[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
)

if __name__ == "__main__": # Manual test run
    logging.info("Running RNN")
    influx_host = os.getenv("INFLUXDB_HOST"),
    influx_token = os.getenv("INFLUXDB_TOKEN"),
    influx_org = os.getenv("INFLUXDB_ORG"),
    influx_bucket = os.getenv("INFLUXDB_BUCKET")
    
    assert influx_host
    assert influx_token
    assert influx_org
    assert influx_bucket


    db = DbReader(
        influx_host,
        influx_token,
        influx_org,
        influx_bucket,
    )

    start = datetime(year=2016, month=1, day=2)
    stop = start + relativedelta(days==+1)
    data = db.read("FT1_122", start, stop)

    rnn = RNN()
    predicted_values = rnn.predict(data)
    # Avgjør hva som er alarm og ikke

    # F.eks plot verdier for denne demoen