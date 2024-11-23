from fastapi import FastAPI, UploadFile, HTTPException, Path
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated, List
from util import create_zip_file
from pydantic import BaseModel
import os

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DIRECTORY = os.getenv("DIR", "../output")

@app.get("/download/{doc_id}")
async def download_file(
    doc_id: Annotated[str, Path(title="File id of converted PDF.")]
):
    try:
        dir = os.path.abspath(DIRECTORY)
        files = os.listdir(dir)
        for f in files:
            if f == doc_id:
                file_path = os.path.abspath(os.path.join(DIRECTORY,f))
                return FileResponse(file_path)
        return HTTPException(status_code=404, detail="No file with this id exists")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cannot Download File {e}")

class BulkDownload(BaseModel):
    files: List[str]


@app.post("/download-bulk")
async def download_bulk_files(data: BulkDownload):
    try:
        print(data)
        dir = os.path.abspath(DIRECTORY)
        files = os.listdir(dir)
        file_path_list = []
        for f in data.files:
            if f in files:
                file_path = os.path.abspath(os.path.join(DIRECTORY,f))
                file_path_list.append(file_path)
        zip = create_zip_file(file_path_list, dir)
        if zip:
            return FileResponse(zip)
        return HTTPException(status_code=404, detail="No file with this id exists")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Cannot Download ZIP File {e}")
