all: run

run:
	uvicorn main:app --host 0.0.0.0 --reload --port 8001

docker:
	docker build -t storage . && docker run -p 11011:11011 --name doc2pdf-storage storage
