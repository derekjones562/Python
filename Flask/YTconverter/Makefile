

run:
	docker-compose --file ./build/docker-compose.yml --project-directory . pull
	docker-compose --file ./build/docker-compose.yml --project-directory . up --build; \
	docker-compose --file ./build/docker-compose.yml --project-directory . down --volumes;