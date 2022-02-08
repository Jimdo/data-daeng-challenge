# Data Engineering Test

We as a data engineering team at Jimdo gather data from various sources, transform the collected data and deliver it to our stakeholders.
We collect a lot of data from various APIs, 3rd party sources and our own backend databases and tracking systems. We then process it, transform it and load it to our data-warehouse.

We want to create a new table `dash.statistics` in our datawarehouse, which populates the data from our `dash` API. 
Our expectation for this test is to write an ETL Pipeline that fetches data from the dash API endpoint, create DDL statement and able to query from our new table.


### Setup 
In this challenge, the expectation is you already have installed docker on your machine. Otherwise, please check this [documentation](https://docs.docker.com/get-docker/ )  to install the docker.
Before start writing the ETL pipeline you need to start the 2 docker services `postgres-db` and `dash_statistics_service`
via 

`docker-compose up --build` 

This will run two service 
`postgres-db: host: postgres port=5432 database: dwh  user: postgres`
`dash_statistics_service: host: 0.0.0.0 port: 5000 endpoint: /v1/dash/statistics` 




# Challenge

## 1) To create ETL Pipeline 

In this part, you have to create a small ETL pipeline that gets websites `statistics` data from `dash` API. 
host: `localhost:5000` endpoint: `/v1/dash/statistics` 

1. Extract data from API endpoint  
2. Load the, extracted data to PostgreSQL 
3. You need to create First Schema `dash` and Table  `statistics` for this data 

The API returns the list of JSON objects in the following format:
```
{
    "statistics": [
        {
            "clicked_booking_button": 8,
            "date": "2022-01-27",
            "engaged_visitors": 28,
            "sent_contact_form": 8,
            "sources": {
                "direct": 43,
                "facebook": 17,
                "google": 25
            },
            "top_pages": {
                "/": 68,
                "/about": 25,
                "/privacy-policy": 17
            },
            "visitors": 86,
            "visits": 103,
            "website_id": "4149179c-3745-46be-a4d9-c9b92b0f378d"
        },
        ....
        ....
        ....
    ]
}
```
You can connect to any Database tool like DBeaver or can use this script to 
` docker exec -it postgres psql -U Postgres -d dwh` 
and connect to psql inside the postgres container.
Now you can create your schema and table according to the response data.



We have created a folder for your ETL pipeline in `etl_job`.  We have created Python Projectwith  as a quick start for you but you are free to choose any language which you are comfortable most.
this directory has following structure
 

```
etl_job:
    - app
        - main.py
    - Dockerfile
    - requirements.txt
```


### Run etl_job locally

We have  already setup Dockerfile for the python job you need to build it and run it locally to check the results 
`docker build -t my_job:latest . `

`docker run --name dash_statistic_job  my_job:latest `


,
## 2) Query from Database
In this part, we are expecting to write SQL queries:

`Select all website which has more direct visits than other sources i.e. (facebook,google) `
 
 
##Evaluation:
In the end, you'll be evaluated based on your DDL statement, python code and SQL Query.
