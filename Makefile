all: run

run:
	uvicorn main:app --host 0.0.0.0 --reload --port 8001

docker:
	docker build -t fastapi-app . && docker run -p 11011:11011 fastapi-app
