# -*- coding: utf-8 -*-
from datetime import datetime
import logging
from influxdb_client import InfluxDBClient

class DbReader:
    def __init__(self, host, token, org, bucket):
        logging.info("Initializing db connection, host: %s, org: %s, bucket: %s", host, org, bucket)
        self.client = InfluxDBClient(url=host, token=token, org='Leakdetection')
        self.query_api = self.client.query_api()
        self.bucket = bucket
        self.org = org
    
    def read(self, tag, start: datetime, stop: datetime):
        query = '''from(bucket: "{bucket}")\
                |> range(start: {start}, stop: {stop})\
                |> filter(fn: (r) => r["_measurement"] == "flow")\
                |> filter(fn: (r) => r["_field"] == "value")\
                |> filter(fn: (r) => r["tag"] == "{tag}")\
                |> keep(columns: ["_time", "_value"]) \
                '''.format(bucket=self.bucket, start=start.strftime('%Y-%m-%dT%H:%M:%SZ'), stop=stop.strftime('%Y-%m-%dT%H:%M:%SZ'), tag=tag)
        return self.query_api.query_data_frame(query=query)