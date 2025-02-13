import random
import pandas as pd
from typing import List, Dict

class SecretSantaAssigner:
    def __init__(self, employees: List[Dict[str, str]], last_year: Dict[str, str]):
        self.employees = employees
        self.last_year = last_year

    def assign_secret_santa(self) -> List[Dict[str, str]]:
        available_children = [e["Employee_EmailID"] for e in self.employees]
        assignments = []

        for employee in self.employees:
            possible_children = [
                child for child in available_children
                if child != employee["Employee_EmailID"] and child != self.last_year.get(employee["Employee_EmailID"])
            ]

            if not possible_children:
                raise ValueError("Unable to assign Secret Santa due to constraints.")

            secret_child = random.choice(possible_children)
            available_children.remove(secret_child)

            child_details = next(e for e in self.employees if e["Employee_EmailID"] == secret_child)
            assignments.append({
                "Employee_Name": employee["Employee_Name"],
                "Employee_EmailID": employee["Employee_EmailID"],
                "Secret_Child_Name": child_details["Employee_Name"],
                "Secret_Child_EmailID": child_details["Employee_EmailID"],
            })
        
        return assignments
