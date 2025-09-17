from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title="Artigos Api - JWT Auth")
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

''''
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzU4NjUwMzA3LCJpYXQiOjE3NTgwNDU1MDcsInN1YiI6IjEifQ.av7RhIAMQv71IYRDbVq490ThwOOGrGeIw1kaWsVhTMs
tipo : bearer 

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNjZXNzX3Rva2VuIiwiZXhwIjoxNzU4NjYyMzQ4LCJpYXQiOjE3NTgwNTc1NDgsInN1YiI6IjIifQ.Mrd52-3sgfi58d2R7KdT-e-qBf80dpMgmLT633E84o4

'''