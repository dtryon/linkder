from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    # hello
    return {"message": "Hello World"}
