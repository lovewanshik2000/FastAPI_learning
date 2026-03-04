from fastapi import FastAPI, Path, HTTPException, Query
import json
app = FastAPI()

# Create a helper function to load the patient data from the JSON file
def load_patient_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

# Create an endpoint to get all patient data
@app.get("/")
def welcome():
    return {"message": "Welcome to the Patient Record Management System!"}

@app.get("/view")
def view():
    data = load_patient_data()
    return {"status": "success","data": data}


@app.get("/view/{patient_id}")
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve from the DB.", example="P001")):
    data = load_patient_data()
    if patient_id in data:
        return {"status": "success","data": data[patient_id]}
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight,bmi,age"), order: str = Query('asc', description="Sort in ascending or descending order", examples={"asc": {"summary": "Ascending order"}, "desc": {"summary": "Descending order"}})):
    valid_fields = ['height', 'weight', 'bmi', 'age']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort_by value. Must be one of {valid_fields}")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order value. Must be 'asc' or 'desc'")
    
    data = load_patient_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=sort_order)
    
    return {"status": "success","data": sorted_data}
    