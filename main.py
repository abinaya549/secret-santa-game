from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import shutil
from pathlib import Path
from src.santa_assigner import SecretSantaAssigner
from src.file_handler import read_csv, write_csv

# Initialize FastAPI app
app = FastAPI()

# directory create to store uploaded files
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

@app.post("/process_secret_santa/")
async def process_secret_santa(
    employees: UploadFile = File(...), last_year: UploadFile = File(...)
):
    """
    API to upload files, process Secret Santa assignments, and return results in one call.
    """
    
    # file paths
    emp_file_path = DATA_DIR / "employees.csv"  #company employee details
    last_year_path = DATA_DIR / "last_year.csv" #pervious year santa game csv
    output_file_path = DATA_DIR / "output.csv"

    # Save uploaded files
    with open(emp_file_path, "wb") as buffer:
        shutil.copyfileobj(employees.file, buffer)

    with open(last_year_path, "wb") as buffer:
        shutil.copyfileobj(last_year.file, buffer)

    # Read CSVs
    try:
        employees_data = read_csv(emp_file_path)
        last_year_data = read_csv(last_year_path)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error reading CSV files: {str(e)}")

    last_year_dict = {row["Employee_EmailID"]: row["Secret_Child_EmailID"] for row in last_year_data}

    try:
        assigner = SecretSantaAssigner(employees_data, last_year_dict)
        assignments = assigner.assign_secret_santa()
        write_csv(output_file_path, assignments)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    #download link hardcode
    download_link = f"http://127.0.0.1:8000/download/output.csv"

    return {
        "message": "Secret Santa assignments completed successfully",
        "download_link": download_link
    }

@app.get("/download/output.csv")
async def download_results():
    """
    API to download the Secret Santa assignment results csv.
    """
    output_file_path = DATA_DIR / "output.csv"
    if not output_file_path.exists():
        raise HTTPException(status_code=400, detail="No assignment results found.")
    
    return FileResponse(output_file_path, filename="secret_santa_results.csv")


# Run the app when executing main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
