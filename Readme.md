## Storage Service

This service is responsible for storing and retrieving files from the file system.

There are 2 routes defined in this service:
- /download/{doc id} - which gives a link to the pdf doc from where it can be downloaded
- /download-bulk - it is post request which takes a list of doc ids and returns a zip file containing all the pdfs

## Instructions to run

- `pip install -r requirements.txt` to install the dependencies
- `make` to run the server
- `make docker` to build and run the docker image
