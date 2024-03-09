from fastapi import FastAPI
from typing import Any
from pydantic import BaseModel, Json
from app.model.model import predict_model
from app.model.model import __version__ as model_version
import pandas as pd
import numpy as np 

app = FastAPI()

class Customer(BaseModel):
    age: int
    occupation: str
    marital_status: str
    education: str
    has_credit: str
    housing_loan: str
    personal_loan: str
    contact_mode: str
    month: str
    week_day: str
    last_contact_duration: int
    contacts_per_campaign: int
    N_last_days: int
    nb_previous_contact: int
    previous_outcome: str
    emp_var_rate: float
    cons_price_index: float
    cons_conf_index: float
    euri_3_month: float
    nb_employees: float

@app.get("/")
async def home():
    return {"Model status": "OK", "model_version": model_version}

@app.post("/predict")
async def predict(customer: Customer):
    customer = pd.json_normalize(customer.dict())
    will_subscribe = predict_model(customer)
    answer = "No" if will_subscribe==np.array([0]) else "Yes"
    return {"Will the user subscribe:": answer}
