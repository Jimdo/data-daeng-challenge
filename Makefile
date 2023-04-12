.PHONY: start
start:
	docker-compose up

.PHONY: query-api
query-api:
	curl http://localhost:5000/v1/dash/statistics | jq '.'

.PHONY: run
run:
	cd etl_job && docker build -t etl_job .
	docker run \
		--rm \
		-it \
		--network="host" \
		-v $(shell pwd)/etl_job/app:/app \
		etl_job
