from pydantic import BaseModel
# fast api model

class CustomerData(BaseModel):
    tenure:int
    MonthlyCharges:float
    TotalCharges:float
    SeniorCitizen:float
# its for validation