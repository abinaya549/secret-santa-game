# Secret Santa Game - FastAPI 

## Project Overview
This FastAPI-based Secret Santa application automates the process of assigning Secret Santa pairs while ensuring fairness and avoiding last year's matches.

## Features
Upload employee and last year's assignment CSVs  
Automatically assign Secret Santa pairs  
Prevent employees from being assigned the same Secret Child as last year  
Download results in CSV format 

## Start the FastAPI server using Uvicorn:
Before that create Virtual Environment and activated in ur local machine.
Install requirements.txt file
# run the main.py file
python main.py

## API Endpoints

## Need to upload the employee csv and previous year santa game csv and after upload hitting the url its provide you a secret santa game csv.

url: "http://127.0.0.1:8000/process_secret_santa/"	

Method - POST

payload = {}
files=[
    "employees":
    "last_year":
]

response:
{
    "message": "Secret Santa assignments completed successfully",
    "download_link": "http://127.0.0.1:8000/download/output.csv"
}

## This api download the csv file.

url: "http://127.0.0.1:8000/download/output.csv"	

Method - GET





