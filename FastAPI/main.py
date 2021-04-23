"""
pip install fastapi
pip install hypercorn
pip install uvicorn
pip install requests
python -m hypercorn main:app --reload (To execute)
python -m uvicorn main:app --reload (To execute)

DOCUMENTATION
=============
(Swagger)
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc

"""
from fastapi import FastAPI
from pydantic import BaseModel
import requests


db = []

# Model
class City(BaseModel):
    name: str
    timezone: str

app = FastAPI()

@app.get("/")
def index():
    return {"key":"value"}


@app.get("/cities")
def get_cities():
    results = []
    for city in db:
        r = requests.get(f"http://worldtimeapi.org/api/timezone/{city['timezone']}")
        print(r.json())
        current_time = r.json()['datetime']
        results.append({'name': city['name'], 'timezone': city['timezone'], "current_time": current_time})
    return results

@app.get("/cities/{city_id}")
def get_city(city_id: int):
    return db[city_id-1]


@app.post("/cities")
def create_city(city: City):
    db.append(city.dict())
    return db[-1]


@app.delete("/cities/{city_id}")
def delete_city(city_id: int):
    db.pop(city_id-1)
    return {}
























