import pandas as pd
from typing import List, Dict

def read_csv(file_path: str) -> List[Dict[str, str]]:
    """Reads a CSV file and returns a list of dictionaries."""
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")

def write_csv(file_path: str, data: List[Dict[str, str]]):
    """Writes a list of dictionaries to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
