PYTHONPATH=./sp_py/

build:
	docker stop sp_db_c1 || true
	docker rm sp_db_c1 || true
	docker-compose up -d 
	sleep 4
test:
	pytest --ignore=sp_db_data_volume

.PHONY: build test

