from fastapi import FastAPI
from api.ozon import ozon_router

# RUN FAST API - uvicorn main:app --reload

app = FastAPI()

app.include_router(ozon_router)


@app.get("/")
def test():
    return {'test': 'OK'}
