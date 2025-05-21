from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI ()

app.add_middleware (
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get ("/")
def index ():
    return {
        "messsage": "Welcome to the FastAPI application!",
    }

@app.get ("/api/params")
def search (request: Request):
    parameters = list ()

    for parameter_name in request.query_params.keys ():
        parameters.append (parameter_name)

    print (parameters)

    return {
        "parameters": parameters,
    }
