from fastapi import FastAPI
from api.recommendations import router

app = FastAPI(title="Travel Planner API")

app.include_router(router)

@app.get("/")
def root():
    return {
        "message": "Travel Planner Backend Running"
    }