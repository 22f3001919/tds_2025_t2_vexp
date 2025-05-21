from fastapi import FastAPI, Request

app = FastAPI ()

@app.get ("/")
def index ():
    return {
        "messsage": "Welcome to the FastAPI application!",
    }

