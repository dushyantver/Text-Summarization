import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "TextSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep", # helpful for CI/CD Deployment
    f"src/{project_name}/__init__.py",  ## for local system installation
    f"src/{project_name}/component/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)   ## it will detect the os a/c to that path will be created
    filedir, filename = os.path.split(filepath)   ## split the file directory and file name

    if filedir != "":                           ## it will check whether folder is there or not 
        os.makedirs(filedir, exist_ok=True)         ## if not than it will create one
        logging.info(f"creating directory: {filedir} for the {filename}")   ## logging will show on terminal

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists.")