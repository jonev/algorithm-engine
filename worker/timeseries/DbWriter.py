# -*- coding: utf-8 -*-
import logging
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from influxdb_client.domain.write_precision import WritePrecision


class DbWriter:
    def __init__(self, host, token, org, bucket):
        logging.info("Initializing db connection, host: %s, org: %s, bucket: %s", host, org, bucket)
        assert host
        assert token
        assert org
        assert bucket
        self.client = InfluxDBClient(url=host, token=token, org=org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)
        self.bucket = bucket

    def writePointRaw(self, measurement, tag, location, value, unit, timestamp):
        logging.debug("Writing point, tag: %s, location: %s, value: %s, unit: %s, timestamp: %s",
                     tag, location, value, unit, timestamp)
        point = self.__valueObject__(measurement, tag, location, value, unit, timestamp)
        self.write_api.write(bucket=self.bucket, record=point, write_precision=WritePrecision.MS)

    def __valueObject__(self, measurement, tag, location, value, unit, timestamp):
        return Point(measurement) \
                    .tag("tag", tag)    \
                    .tag("location", location)  \
                    .field("value", value)  \
                    .field("unit", unit)    \
                    .time(timestamp, \
                    write_precision=WritePrecision.MS)
