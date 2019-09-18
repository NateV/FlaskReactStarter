

.PHONY: docker
docker:
	cd server/static && npm run build
	sudo docker build --tag=$(tag) .