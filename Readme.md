## Storage Service

This service is responsible for storing and retrieving files from the file system.

There are 2 routes defined in this service:
- /download/{doc id} - which gives a link to the pdf doc from where it can be downloaded
- /download-bulk - it is post request which takes a list of doc ids and returns a zip file containing all the pdfs

## Instructions to run

- `python3 -m venv venv` to create the virtual env.
- `source venv/bin/activate` to activate the virtual env.
- `pip install -r requirements.txt` to install the dependencies
- `make` to run the server
- `make docker` to build and run the docker image

## Technologies/Libraries Used

- Python
- FastAPI
- zipfile

## Running the stack

To run the whole stack, use this [Dockerfile](https://github.com/Doc2PDF/deployments/blob/main/docker-compose.yaml).
`docker compose up -d --build`

## Creating New Releases

To create a new release of the app, push a new tag of format `v*` to the repository. The github actions will automatically create a new release and push the docker image to the docker hub.

- `git tag v1.0.0`
- `git push origin v1.0.0`
