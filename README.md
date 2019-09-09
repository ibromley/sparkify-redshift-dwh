# Sparkify Redshift Data Warehouse

A Redshift data warehouse for understanding the listing habits of Sparkify users


## Purpose
This database serves analytical data repository for Sparkify, a startup which building a new music streaming application. They intend to perform analytics on understand the listening habits of their users. Ideally, the want to know which users are playing certain songs and further gather all relevant metadata about the track played.

## Setup

### Requirements

You'll need this software installed on your system 
* [PostgreSQL](https://www.postgresql.org/download/)
* [Python](https://www.python.org/downloads/)

In addition you'll need the PostgreSQL python driver which can be obtained via `pip`
```
pip install psycopg2 
```

### Quick Start
Create the database tables by running the `create_tables.py` script, followed by `etl.py` to perform the data loading.

```
> python create_tables.py 
> python etl.py
```
Optionally a PostgreSQL client (or `psycopg2`) can be used to connect to the Sparkify db to perform analytical queries afterwards.