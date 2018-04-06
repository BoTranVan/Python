#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# @author: ministry
try:
    import psycopg2
except ImportError as e:
    raise e

    

__defautlConfig__ = {
    "host": "localhost",
    "port": "5432",
    "database": "postgres",
    "user": "postgres",
    "password": "postgres"
}

def _connectDatabase():
    conn = psycopg2.connect()