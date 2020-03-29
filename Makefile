build:
	mkdir sp_db_data_volume
	docker stop sp_db_c1 || true
	docker rm sp_db_c1 || true
	docker-compose up 
	sleep 2

.PHONY: build

