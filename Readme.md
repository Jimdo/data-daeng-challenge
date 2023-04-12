# Data Engineering Test

The data engineering team at Jimdo needs to: 
- Gather data from various sources
- Transform the collected data
- Deliver it to our stakeholders

In this exercise, we want to pull data from our Website Statistics API and
provide a new table  `dash.statistics` that allows to query the statistics data.  


- [ ] Query the statistics data from the API endpoint
- [ ] Design the table structure with our use case in mind (see below)
- [ ] Write the DDL to create the table(s) 
- [ ] Ingest the data in the table structure you've designed
- [ ] Query the database you created


### Setup 

Expected tools

- Docker
- Python environment
- SQL 

In this challenge, the expectation is you already have installed docker on your machine. Otherwise, please check this [documentation](https://docs.docker.com/get-docker/ )  to install the docker.
Before start writing the ETL pipeline you need to start the 2 docker services `postgres-db` and `dash_statistics_service`
via 

`docker-compose up --build` 

This will run two service 
`postgres-db: host: postgres port=5432 database: dwh  user: postgres`
`dash_statistics_service: host: 0.0.0.0 port: 5000 endpoint: /v1/dash/statistics` 




# Challenge

Use case: 

We want to identify all websites that have more direct visits than visits from
all other sources i.e. (facebook,google) combined.



## 1) To create ETL Pipeline 

In this part, you have to create a small ETL pipeline that gets websites `statistics` data from `dash` API. 
host: `localhost:5000` endpoint: `/v1/dash/statistics` 

1. Extract data from API endpoint  
2. Load the, extracted data to PostgreSQL 
3. You need to create First Schema `dash` and Table  `statistics` for this data 

The API returns the list of JSON objects in the following format:

```json
{
    "statistics": [
        {
            "website_id": "4149179c-3745-46be-a4d9-c9b92b0f378d",
            "date": "2022-01-27",
            "sources": {
                "direct": 43,
                "facebook": 17,
                "google": 25
            },
            "visitors": 86,
            "visits": 103,
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

`Select all websites which have more direct visits than all the other sources i.e. (facebook,google) combined`
 
 
##Evaluation:
In the end, you'll be evaluated based on your DDL statement, python code and SQL Query.
