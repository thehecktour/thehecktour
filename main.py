from fastapi import FastAPI

app = FastAPI()

@app.get("/api/v1/users")
def read_root():
    return {"Hello": "World"}
