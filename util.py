from typing import List
from zipfile import ZipFile
from uuid import uuid4
import os

def create_zip_file(paths: List[str], dir: str):
    zip_name = os.path.join(dir, f'converted_files-{uuid4()}.zip')
    with ZipFile(zip_name, 'w') as zip:
        for file in paths:
            zip.write(file, arcname=os.path.basename(file))
    return zip_name
