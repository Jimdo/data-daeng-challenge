# Data Engineering Test

The data engineering team at Jimdo needs to: 
- Gather data from various sources
- Transform the collected data
- Deliver it to our stakeholders

In this exercise, we want to pull data from our Website Statistics API and
provide a new table `dash.statistics` that allows to query the statistics data.  

Your tasks:

- [ ] Query the statistics data from the API endpoint
- [ ] Design the table structure with our use case in mind (see below)
- [ ] Ingest the data in the table structure you've designed
- [ ] Query the database you created


## Setup 

Expected tools

- Docker, docker-compose
- Python environment
- SQL client
- curl, jq

This will run two services
`postgres-db: host: postgres port=5432 database: dwh  user: postgres`
`dash_statistics_service: host: 0.0.0.0 port: 5000 endpoint: /v1/dash/statistics` 

```bash
make start
```

You can query this API and view the returned data with this command.

```bash
make query-api
```

## Challenge

Use case: 

We want to identify all websites that have more direct visits than visits from
all other sources i.e. (facebook,google) combined.

### 1) Query the statistics data from the API endpoint

In `etl_job/app/main.py`, write the Python code needed to fetch results from the API.

```text
http://localhost:5000/v1/dash/statistics
```

You can execute the ETL job by running:

```bash
make run
```

### 2) Design the table structure with the use-case in mind

Remember:
> We want to identify all websites that have more direct visits than visits from all other sources i.e. (facebook,google) combined.

```SQL
create table dash.statistics (
  website_id uuid,
  date date,
  ...
);
```

Here's the API result for convenience:

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

### 3) Ingest data into the newly created table using Python

You'll need to transform the API data into the format matching your designed `dash.statistics` table.

You can execute the ETL job by running:

```bash
make run
```

### 4) Query your table to answer the use-case

Remember:
> We want to identify all websites that have more direct visits than visits from all other sources i.e. (facebook,google) combined.

 
## Evaluation

In the end, you'll be evaluated based on your DDL statement, Python code and the SQL Query.
